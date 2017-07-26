new_form = '<div class="main">' +
  '<h2>Date and Time</h2>/n'+
  '<input type= "date" name = "date_test"></input>'+
  '<input type= "time" name= "time_test"></input>'+
  '<h2>Email</h2>'+
  '<input type= "email" name="email_test"></input>'+
  '<h2>Name of Event</h2>'+
  '<input type= "name_of_event" name="name_test" id= "name_event"/>'+
  '<h2>Where</h2>'+
  '<input type= "Where" name="where_test" id= "where_event"/>'+
  '<h2>Latitude and Longitude</h2>'+
  '<input type= "Latitude" name="latitude_test" id= "where_event"/>'+
  '<input type= "Longitude" name="longitude_test" id= "where_event"/>'+
  '<h2>Description of Event</h2>'+
  '<input type= "description_of_event" name="description_test" id= "description_event"/>'

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
  $('.main').eq(-1).remove();
}

function add_event(event) {
  new_event = $("#Create_box").append(new_form);
  console.log("new event has been added");
  $('.main').append();
}

function interrupt_submit(event){

  console.log("New Event Form has been submitted")

  return false
}
