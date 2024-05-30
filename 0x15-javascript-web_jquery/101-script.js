/*
 Uses JQuery to easily modify the DOM using event handlers
*/

$(document).ready(() => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</item>');
  });

  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').on('click', () => {
    $('UL.my_list li').remove();
  });
});
