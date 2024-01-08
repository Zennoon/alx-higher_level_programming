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
	int len = 0, i;
	listint_t *ptr = *head, *iter = *head;

	while (ptr)
	{
		ptr = ptr->next;
		len++;
	}
	len--;
	while (len > 0)
	{
		ptr = iter;
		for (i = 0; i < len; i++)
			ptr = ptr->next;
		if (iter->n != ptr->n)
			return (0);
		iter = iter->next;
		len -= 2;
	}
	return (1);
}
