function createNewEvent() {
  $('#remove_event').on('click' , remove_last_event);
}
function associate_events(  ) {
  $('#remove_event').on('click', remove_last_event);
  $('#add_event').on('click', add_event);
  $('#submit_button').click(interrupt_submit)
  console.log('ready')
}

$(document).ready(
   associate_events
   //once its loaded the fcn above will appear
);
function remove_last_event(event) {
  console.log("last event was removed");
  $('#main').eq(-1).remove();
}

function add_event(event) {
  new_event = $("#main").append(new_item);
  console.log("new event has been added");
  $('#main').append();
}

function interrupt_submit(event){
  
  console.log("New Event Form has been submitted")

  return false
}
