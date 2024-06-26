document.getElementById("inputFile").addEventListener("change", function () {
    var fileList = document.getElementById("fileList");
    fileList.innerHTML = "";
    var files = this.files;
    for (var i = 0; i < files.length; i++) {
        var li = document.createElement("li");
        li.textContent = files[i].name;
        fileList.appendChild(li);
    }
});

const btn = document.querySelector(".buttonSubmit");
btn.addEventListener("click", () => {
    const fileInput = document.querySelector("#inputFile");
    if (fileInput.files.length === 0) {
        alert("Please select a file");
        return;
    }
    const files = fileInput.files;
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
    }

    fetch("http://localhost:8080/upload", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then(() => {
            alert(`Upload success`);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
