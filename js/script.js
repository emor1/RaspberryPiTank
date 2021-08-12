function showView(event) {
    view.removeAttribute('hidden');
    view.style.left = event.clientX - 50 + 'px';
    view.style.top = event.clientY - 50 + 'px';
    event.preventDefault();
}

function moveView(event) {
    view.style.left = event.clientX - 50 + 'px';
    view.style.top = event.clientY - 50 + 'px';
    if ((event.clientY - 50)>60){
        tankCmd("forward");
    }
}

function hideView(event) {
    view.setAttribute('hidden', '');
}

const container = document.querySelector('.container');
const view = document.querySelector('.view');

container.onmousedown = showView;
container.onmousemove = moveView;
document.onmouseup = hideView;

function tankCmd(way) {
    let form = document.createElement("form");
    form.setAttribute("action", "/on");
    form.setAttribute("method", "post");
    form.setAttribute("target", "hiddeniframe");
    form.style.display = "none";
    console.log(way);
    document.body.appendChild(form);

    let input;
    input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "name");
    input.setAttribute("value", way);

    form.appendChild(input);
    form.submit();
}

