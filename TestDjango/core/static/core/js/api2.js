const aplication = document.querySelector('.container')

const url = 'http://127.0.0.1:8000/api/lista_usua'

fetch(url)
.then(response => response.json())
.then(data => {
    data.forEach(usuario =>{
        const n = document.createElement('n')
        n.innerHTML = usuario.nombre
        aplication.appendChild(n)

        const e = document.createElement('e')
        e.innerHTML = usuario.email
        aplication.appendChild(e)

        const c = document.createElement('c')
        c.innerHTML = usuario.contraseña
        aplication.appendChild(c)
    })
    console.log(data)
})
.catch(err => console.log(err))