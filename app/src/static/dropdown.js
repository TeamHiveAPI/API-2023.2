document.getElementById("dropdown_centros").addEventListener("change", mostrar_dados)

function mostrar_dados() {

    let regiao = document.getElementById("dropdown_centros").value

    let dados_norte = document.getElementById("dados_norte")
    let dados_nordeste = document.getElementById("dados_nordeste")
    let dados_centro_oeste = document.getElementById("dados_centro_oeste")
    let dados_sudeste = document.getElementById("dados_sudeste")
    let dados_sul = document.getElementById("dados_sul")

    if (regiao == "norte") {
        dados_norte.classList.add("mostrar")
    }
    else {
        dados_norte.classList.remove("mostrar")
    }

    if (regiao == "nordeste") {
        dados_nordeste.classList.add("mostrar")
    }
    else {
        dados_nordeste.classList.remove("mostrar")
    }

    if (regiao == "centro_oeste") {
        dados_centro_oeste.classList.add("mostrar")
    }
    else {
        dados_centro_oeste.classList.remove("mostrar")
    }

    if (regiao == "sudeste") {
        dados_sudeste.classList.add("mostrar")
    }
    else {
        dados_sudeste.classList.remove("mostrar")
    }

    if (regiao == "sul") {
        dados_sul.classList.add("mostrar")
    }
    else {
        dados_sul.classList.remove("mostrar")
    }


}

document.getElementById("dropdown_centros_dialise").addEventListener("change", mostrar_dados_dialise)

function mostrar_dados_dialise() {

    let regiao = document.getElementById("dropdown_centros_dialise").value

    let dados_norte = document.getElementById("dados_norte_dialise")
    let dados_nordeste = document.getElementById("dados_nordeste_dialise")
    let dados_centro_oeste = document.getElementById("dados_centro_oeste_dialise")
    let dados_sudeste = document.getElementById("dados_sudeste_dialise")
    let dados_sul = document.getElementById("dados_sul_dialise")

    if (regiao == "norte") {
        dados_norte.classList.add("mostrar")
    }
    else {
        dados_norte.classList.remove("mostrar")
    }

    if (regiao == "nordeste") {
        dados_nordeste.classList.add("mostrar")
    }
    else {
        dados_nordeste.classList.remove("mostrar")
    }

    if (regiao == "centro_oeste") {
        dados_centro_oeste.classList.add("mostrar")
    }
    else {
        dados_centro_oeste.classList.remove("mostrar")
    }

    if (regiao == "sudeste") {
        dados_sudeste.classList.add("mostrar")
    }
    else {
        dados_sudeste.classList.remove("mostrar")
    }

    if (regiao == "sul") {
        dados_sul.classList.add("mostrar")
    }
    else {
        dados_sul.classList.remove("mostrar")
    }
}