const URL_USERS = 'https://jsonplaceholder.typicode.com/users';
const URL_POSTS = 'https://jsonplaceholder.typicode.com/posts';
const URL_CATS = 'https://api.thecatapi.com/v1/images/search?limit=10';
const URL_COMMENTS = 'https://jsonplaceholder.typicode.com/comments';

fetch(URL_USERS)
  .then(response => response.json())
  .then(data => mostrarData(data))
  .catch(error => console.log(error));

const mostrarData = (data) => {
  console.log(data);
  let users = '';
  for (let i = 0; i < 10; i++) {
    users += `
      <div class="testimonios-caja">
        <div class="caja-top">
          <div class="perfil">
            <div class="perfil-img">
              <img class="p-img" alt="uwu">
            </div>
            <div class="name-user">
              <strong>${data[i].name}</strong>@${data[i].username}<span></span>
            </div>
          </div>
          <div class="reseñas">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
          </div>
        </div>
        <div class="comentarios-clientes">
          <p></p>
        </div>
      </div>
    `;
  }
  document.querySelector('.testimonios-contenedor').innerHTML = users;
};

fetch(URL_COMMENTS)
  .then(response => response.json())
  .then(data => {
    const comentarios = document.querySelectorAll('.comentarios-clientes');

    // Iterar sobre cada caja de comentarios y asignar el contenido del campo "body"
    comentarios.forEach((comentario, index) => {
      comentario.innerHTML = data[index].body;
    });
  });


fetch(URL_CATS)
  .then(res => res.json())
  .then(data => {
    const cajasComentarios = document.querySelectorAll('.testimonios-caja');

    // Iterar sobre cada caja de comentarios y asignar una imagen diferente
    cajasComentarios.forEach((caja, index) => {
      const img = caja.querySelector('.p-img');
      img.src = data[index].url;
    });
  });


fetch(URL_POST)
  .then(response => response.json())
  .then(posts => {
    const comentariosClientes = document.querySelectorAll('.comentarios-clientes');

    // Iterar sobre cada caja de comentarios y asignar el contenido del campo "body" de la publicación correspondiente
    comentariosClientes.forEach((comentario, index) => {
      comentario.querySelector('p').innerText = posts[index].body;
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });