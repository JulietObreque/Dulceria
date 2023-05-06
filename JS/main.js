const listComments = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/comments");
    const comments = await response.json();

    let tableBody = ``; 
    comments.forEach((comment,foro)=>{
        tableBody += `<tr>
        <td>${comment.name}</td>
        <td>${comment.email}</td>
        <td>${comment.body}</td>
        </tr>`;
    });
    tableBody_Comments.innerHTML = tableBody
};

window.addEventListener("load", function (){
    listComments();
})