$('.chat-form').on('submit', function(e){
  e.preventDefault();
  var msg = $('.chat-box').val(),
      member = $('.member.checked')
      receiver = member.children('input');
  $.ajax({
    url: '/post/',
    type: 'POST',
    data: {msgbox: $('.chat-box').val(),
          receiver: receiver.attr('id')
        },
    success : function(json) {
      $('.chat-box').val('')
      $('.'+json.receiver+'').append('<li class="right-msg">'+ json.msg +'</li>');
      var chatlist = document.getElementById('msglist');
      chatlist.scrollTop = chatlist.scrollHeight
    },
  })
})
function getMessages(){
  if(!scrolling){
    $.get('/message/', function(messages){
      $('.msglist').html(messages);
      var chatlist = document.getElementById('msglist');
      chatlist.scrollTop = chatlist.scrollHeight
      console.log(chatlist.scrollHeight);
    });
  }
  scrolling = false;
}

var scrolling = false
$(function(){
  $('.msglist').on('scroll', function(){
    scrolling = true
  });
  refreshTimer = setInterval(getMessages, 500)
});

$(document).ready(function() {
  $('.send').attr('disabled', 'disabled');
  $('.chat-box').keyup(function() {
    if ($(this).val() != ''){
      $('.send').removeAttr('disabled')
    }
    else {
      $('.send').attr('disabled', 'disabled');
    }
  });
});
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
// $(document).ready(function() {
//   $('.team').click(function() {
//     var key = $('.sender').data('pk')
//     if ((3 % key) == 1){
//       $('.sender').css('background-color', 'red');
//     }
//   });
// });
