(function FillWindow(){
    const html_body = document.getElementsByTagName('body')[0];
    if (html_body.offsetHeight <= window.innerHeight){
        html_body.style.height = "100%";
    }
    else{
        html_body.style.height = "auto";
    }
})();