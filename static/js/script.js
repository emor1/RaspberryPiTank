let joy = new JoyStick('joyDiv');

setInterval(direction,50);

function direction(){
    let dir=joy.GetDir();
    console.log(dir);
    if (dir.includes('N')){
        tankCmd("forward");
        console.log('f');
    }
    else if(dir.includes('S')){
        tankCmd("backward");
        console.log('b');
    }
    else if(dir=='E'){
        tankCmd("right");
    }
    else if(dir=='W'){
        tankCmd('left');
        console.log('le');
    }
    else id(dir=='C'){
        tankCmd('stop')
    }

function tankCmd(way) {
    console.log(way);
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

