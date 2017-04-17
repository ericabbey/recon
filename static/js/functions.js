var source = ""
$(document).ready(function(){
    $('html').niceScroll({
        cursorWidth: 30,
        cursorborder: 0,
        cursorborderradius: 0,
        cursorcolor: '#51ad29',
        zindex: 1000
    });
    $('.chat>ul, .event-map').niceScroll({
        cursorWidth: 0,
        cursorborder: 0,
        cursorborderradius: 0,
        cursorcolor: 'silver',
        zindex: 1000
    })
     $(".button-collapse").sideNav();
     $(".parallax").parallax();
     $('.al-post-filter').dropdown()
     $('#message').trigger('autoresize');
     $('.modal').modal();

     var dd = document.getElementById('date')
     var tt = document.getElementById('datetime')
     if(dd){
       $('#date').formatter({
         'pattern': '{{9999}}-{{99}}-{{99}}',
       })
     }
     if(tt){
       $('#datetime').formatter({
         'pattern': '{{9999}}-{{99}}-{{99}} {{99}}:{{99}}',
       })
     }



    var tracks = $('.list');
    $('.playPause').click(function(){
        tracks.removeClass('active');
        $(this).parent().parent('.list').addClass('active');
        data = $(this).parent('.files').data();
        var audio = document.getElementById('audio'),
            title = $('.info > h3'),
            author = $('.info > h2');
        audio.src = data.src;
        audio.autoplay = true
        title.text(data.title);
        author.text(data.author);
    });

     $('.member').click(function(){
       var member = $('.member'),
           state = $('.member').hasClass('checked');
        if (state = true){
            member.removeClass('checked');
        }
        var i = $(".member").index(this),
            messages = $(".chat>ul");
        console.log(i);
        $(this).addClass('checked');
        $('.unchecked').addClass('checked');
        $('.chat-input').removeClass('unchecked');
        messages.css("display","none");
        // messages.eq(i).css("display","block");
        messages.css("display","block");
    });
});

var cycle = document.getElementById("cycle")
if (cycle) {
    $('.slideshow').cycle({
        fx: 'fadeout',
        timeout: 3000,
        slides: '.slide',
        next: '.slide-next',
        prev: '.slide-prev'
    });
}
var source = $('.overlay');
source.click(function(){
    console.log("clicked")
    src = $(this).data("src");
    data = $(this).data();
    title = data.author+" -- "+ data.title
    $(".title > p").text(title)
    var video = document.getElementById('video');
    video.src = src
    video.autoplay = true
})

//////////////////////////////////////// Raw Javascript /////////////////////////////////////////////
