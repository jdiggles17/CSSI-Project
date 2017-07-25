function createNewEvent() {
  $('#remove_event').on('click' , remove_last_event);
}

function remove_last_event() {
  console.log("last event was removed")
  $('#main').eq(-1);
}

function add_event() {
  console.log("new event has been added")
  $('#main').append();
}
