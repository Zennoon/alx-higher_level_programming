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
	n_arr = malloc(sizeof(int) * len);
	node_ptr = *head;
	while (n_arr && node_ptr)
	{
		n_arr[i] = node_ptr->n;
		node_ptr = node_ptr->next;
		i++;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (n_arr[i] != n_arr[len - 1 - i])
		{
			free(n_arr);
			return (0);
		}
	}
	free(n_arr);
	return (1);
}
