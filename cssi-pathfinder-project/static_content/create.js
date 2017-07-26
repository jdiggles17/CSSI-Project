function createNewEvent() {
  $('#remove_event').on('click' , remove_last_event);
}
function associate_events(  ) {
$('#submit_button').click(interrupt_submit)
console.log('ready')
}

$(document).ready(
   associate_events
   //once its loaded the fcn above will appear
);
function remove_last_event(event) {
  console.log("last event was removed");
  $('#main').eq(-1);
}

function add_event(event) {
  new_event = $("#main").append(new_item);
  console.log("new event has been added");
  $('#main').append();
}

function interrupt_submit(event){
  console.log("submit inturrupted")

  return false
}
