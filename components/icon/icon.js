(function () {
    document.querySelectorAll('.icon-container').forEach(function (icon) {
        // get the icon name, it's inside <p>
        const iconName = icon.querySelector('p').innerHTML
        icon.addEventListener('click', function () {
            alert(`Hello, I'm ${iconName}`)
        })
    })
})()