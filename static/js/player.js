// var for audio content

var audio = document.getElementById('audio');

// html5 function - toggle play/pause btn and audio

$("#plays_btn").click(function() {

    if (audio.paused == false) {
        audio.pause();
        $("#play_btn").show();
        $("#pause_btn").hide();
    } else {
        audio.play();
        $("#play_btn").hide();
        $("#pause_btn").show();
    }
});


// function for timeline

audio.addEventListener("timeupdate", function() {
    var currentTime = audio.currentTime,
        duration = audio.duration,
        currentTimeMs = audio.currentTime * 1000;
    $('.progressbar_range').stop(true, true).animate({'width': (currentTime + .25) / duration * 100 + '%'}, 250, 'linear');
});


// count function for timeleft

audio.addEventListener("timeupdate", function() {
    var timeleft = document.getElementById('timeleft'),
        duration = parseInt( audio.duration ),
        currentTime = parseInt( audio.currentTime ),
        timeLeft = duration - currentTime,
        s, m;
    
    s = timeLeft % 60;
    m = Math.floor( timeLeft / 60 ) % 60;
    
    s = s < 10 ? "0"+s : s;
    m = m < 10 ? "0"+m : m;
    
    $('#timeleft').text("-"+m+":"+s);
    
});

var volume = document.getElementById("volume_btn")
volume.onclick=function(){
    if (audio.muted){
        audio.muted = false;
        volume.style.fill = "#51ad29";
    } else {
        audio.muted = true;
        volume.style.fill = "gray";
    }
}

var loop = document.getElementById("shuffle_btn");
loop.style.fill = "gray";
loop.onclick=function(){
    if(audio.loop){
        audio.loop = false;
        loop.style.fill = "gray";
    }else{
        audio.loop = true;
        loop.style.fill = "#51ad29"
    }
}
var backward = document.getElementById("prev_btn");
backward.onclick = function(){
    audio.currentTime = audio.currentTime - 3
}

var forward = document.getElementById("next_btn");
forward.onclick = function(){
    audio.currentTime = audio.currentTime + 3
}
