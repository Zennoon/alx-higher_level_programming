#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a cycle is present in a linked list
 * @head: Pointer to the head (first node) of the list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *head)
{
	listint_t *one_step;
	listint_t *two_step;

	one_step = head;
	two_step = head;
	while (one_step != NULL && two_step != NULL)
	{
		one_step = one_step->next;
		two_step = two_step->next;
		if (two_step != NULL)
			two_step = two_step->next;
		if (one_step == two_step && (one_step != NULL))
			return (1);
	}
	return (0);
}
