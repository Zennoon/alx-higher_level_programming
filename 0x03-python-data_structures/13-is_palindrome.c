#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a given singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, *n_arr;
	listint_t *node_ptr = *head;

	while (node_ptr)
	{
		node_ptr = node_ptr->next;
		len++;
	}
	if (len <= 1)
		return (0);
	n_arr = malloc(sizeof(int) * (len / 2));
	node_ptr = *head;
	for (i = 0; i < ((len + 1) / 2); i++)
	{
		node_ptr = node_ptr->next;
	}
	if (n_arr != NULL)
	{
		for (i = 0; i < (len / 2); i++)
		{
			n_arr[i] = node_ptr->n;
			node_ptr = node_ptr->next;
		}
		node_ptr = *head;
		for (i = (len / 2) - 1; i >= 0; i--)
		{
			if (node_ptr->n != n_arr[i])
			{
				free(n_arr);
				return (0);
			}
			node_ptr = node_ptr->next;
		}
		free(n_arr);
	}
	return (1);
}
