console.log("load csv javascript")

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function do_upload(file){
    let csrfToken = getCookie('csrftoken');
    const formData = {
        csvfile: file,
    }
    console.log(JSON.stringify(formData))
    fetch(fansUrl, {
        method: 'post',
        headers:{
            "Content-type":"multipart/form-data",
            "X-CSRFToken": csrfToken,
        },
        body: formData}).then(r => r.json())
        .then(data => {
            alert(data);
        });
}

function upload(){

    var uploadBtn = document.getElementById('upload-csv-btn')
    var fileInput = document.getElementById('csv-file-input')

    uploadBtn.addEventListener('click', function(){
        fileInput.click();
    });

    fileInput.addEventListener('change', function(){
        var file = fileInput.files[0];
        if (file){
            do_upload(file);
        }
    });
}

upload();