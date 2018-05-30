


var playbtn,vid,seekslider,curtimetext,durtimetext,mutebtn,volumes, fullscreenbtn,video_controls_bar;

function initializePlayer(){
    vid=document.getElementById("my_video");
    video_controls_bar=document.getElementById("video_controls_bar");
    playbtn=document.getElementById("playpause");
    seekslider=document.getElementById("seekslider");
    curtimetext=document.getElementById("curtimetext");
    durtimetext=document.getElementById("durtimetext");
    mutebtn=document.getElementById("mutebtn");
    volumes=document.getElementById("volumes");
    fullscreenbtn=document.getElementById("fullbtn");

    playbtn.addEventListener("click",palyPause,false);
    fullscreenbtn.addEventListener("click",full_Screen,false);
    mutebtn.addEventListener("click",vidMute,false);
    seekslider.addEventListener("change",vidSeek,false);
    volumes.addEventListener("change",setVolume,false);
    vid.addEventListener("timeupdate",seekTimeupdate,false);
}

window.onload=initializePlayer;

function palyPause(){

    if (vid.paused) {
        vid.play();
        playbtn.src=resurl;
       
    }else
    {
        vid.pause();
       playbtn.src=playurl;
       
    }

}

function vidSeek(){

    var seekTo = vid.duration*(seekslider.value/100);
    vid.currentTime=seekTo;

}

function seekTimeupdate(){

    var nt = vid.currentTime*(100/vid.duration);
    seekslider.value=nt;

    var curmins = Math.floor(vid.currentTime/60);
    var cursecs = Math.floor(vid.currentTime-curmins*60);
    var durmins = Math.floor(vid.duration/60);
    var dursecs = Math.floor(vid.duration-durmins*60);

    if (cursecs<10) {
        cursecs="0"+cursecs;
    }

    if (dursecs<10) {
        dursecs="0"+dursecs;
    }

    if (curmins<10) {
        curmins="0"+curmins;
    }

    if (durmins<10) {
        durmins="0"+durmins;
    }

    curtimetext.innerHTML=curmins+":"+cursecs;
    durtimetext.innerHTML=durmins+":"+dursecs;

}

function vidMute(){
    if (vid.muted) {
        vid.muted=false;
        mutebtn.src=spkurl;
    }else
    {
        vid.muted=true;
        mutebtn.src=muteurl;
    }
}

function setVolume()
{

    vid.volume = volumes.value/100;

}

function full_Screen()
{
    if(vid.requestFullScreen){
        vid.requestFullScreen();
    } else if(vid.webkitRequestFullScreen){
        vid.webkitRequestFullScreen();
    } else if(vid.mozRequestFullScreen){
        vid.mozRequestFullScreen();
    }
}
function exit_fullscreen(){
    if(vid.exitFullscreen)
        vid.exitFullscreen();
    else if(vid.mozCancelFullScreen)
        vid.mozCancelFullScreen();
    else if(vid.webkitExitFullscreen)
        vid.webkitExitFullscreen();
    else if(vid.msExitFullscreen)
        vid.msExitFullscreen();
}

vid.on('mouseout', function(){ 
  video_controls_bar.addClass('vjs-fade-out'); 
});

vid.on('mouseover', function(){ 
  video_controls_bar.removeClass('vjs-fade-out'); 
});