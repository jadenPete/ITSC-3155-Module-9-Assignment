document.getElementById("search-button").addEventListener("click", () => {
	window.location = `/movies?q=${document.getElementById("search-input").value}`
})
