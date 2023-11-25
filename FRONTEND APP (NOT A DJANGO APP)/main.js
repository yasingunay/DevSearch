let loginButton = document.getElementById('login-btn')
let logoutButton = document.getElementById('logout-btn')

let token = localStorage.getItem("token")

if (token){
    loginButton.remove()
}else{
    logoutButton.remove()
}


logoutButton.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location.href = "login.html"
})


let projectsUrl = "http://127.0.0.1:8000/api/projects/"


let getProjects = () => {
    fetch(projectsUrl) // default fetch is a get request
        .then(response => response.json())
        .then(data => {
            buildProjects(data)
        })
}


let buildProjects = (projects) =>{
    let projectsWrapper = document.getElementById("project--wrapper")

    projectsWrapper.innerHTML = ""
    
    for (let i = 0; i < projects.length; i++) {
        let project = projects[i];
        
        let projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}" />

                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}" >&#10004; </strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}" >&#10006; </strong>
                     </div>
                     <i>${project.vote_ratio}% Positive feedback</i>
                     <p>${project.description.substring(0,150)}</p>
                </div>
            </div>
        `

        projectsWrapper.innerHTML += projectCard
    }

    // Add an eventListener
    addVoteEvents()

}


let addVoteEvents=  () => {
    let voteButtons = document.getElementsByClassName("vote--option")

    for (let i = 0; i < voteButtons.length; i++) {
        voteButtons[i].addEventListener('click', (e) =>{
            let token = localStorage.getItem("token")
            console.log(token)

            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: "POST",
                headers:{
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({"value": vote })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                getProjects()
            })

        })
        
    }
}



getProjects()