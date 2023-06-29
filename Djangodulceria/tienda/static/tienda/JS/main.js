let url = 'https://jsonplaceholder.typicode.com/users'
fetch(url)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))

const mostrarData = (data) => {
    console.log(data)
    let users = ``
    for (let i = 0; i<(data.length)-9; i++){
        users += `<strong>${data[i].name}</strong>@${data[i].username}<span></span>`
    }
    document.getElementById('data').innerHTML = users
}
// --------------API imagenes-----------------
 const URL = 'https://api.thecatapi.com/v1/images/search?limit=10'

 fetch(URL)
  .then(res => res.json())
  .then(data => {
     const img = document.querySelector('img.p-img');
     img.src = data[0].url;
  });

