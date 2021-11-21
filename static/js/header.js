window.transitionToPage = (href) => {
    document.querySelector('body').style.opacity = 0
    setTimeout(() => {
        window.location.href = href
    }, 500)
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('body').style.opacity = 1
})