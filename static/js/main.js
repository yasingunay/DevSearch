// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

//ENSURE SEARCH FORM EXISTS
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener("click", function (e) {
            e.preventDefault();

            // GET THE DATA ATTIBUTE
            let page = this.dataset.page;

            // ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

            //SUBMIT FORM
            searchForm.submit();
        });
    }
}

let tags = document.getElementsByClassName("project-tag");

for (let i = 0; i < tags.length; i++) {
    tags[i].addEventListener("click", (e) => {
        let tag_id = e.target.dataset.tag;
        let project_id = e.target.dataset.project;

        fetch("http://127.0.0.1:8000/api/remove-tag/", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ project: project_id, tag: tag_id }),
        })
            .then((response) => response.json())
            .then((data) => {
                e.target.remove();
            });
    });
}
