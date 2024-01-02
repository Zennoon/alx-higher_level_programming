#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a new node in a sorted singly linked list
 * @head: Pointer to a pointer to the head (first node) of the list
 * @number: The number to be included in the new node
 *
 * Return: The address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node != NULL)
	{
		listint_t *ptr = *head;

		new_node->n = number;
		if (*head == NULL || number < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
			while (ptr->next != NULL && ptr->next->n <= number)
				ptr = ptr->next;
			new_node->next = ptr->next;
			ptr->next = new_node;
		}
	}
	return (new_node);
}
