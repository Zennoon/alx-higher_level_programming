/*
 Adds a list item to a list element when another element is clicked
 */

$('DIV#add_item').on('click', () => {
  $('UL.my_list').append('<li>Item</li>');
});
