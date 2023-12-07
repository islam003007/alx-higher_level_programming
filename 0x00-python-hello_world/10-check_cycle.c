#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if the linked list has a cycle.
 *
 * @list: inputs head.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *temp_head = list;
	int i, n = 0;

	while (list != NULL)
	{
		list = list->next;
		n++;
		i = 0;
		temp = temp_head;
		while (temp != list)
		{
			temp = temp->next;
			i++;
		}
		if (n != i)
			return (1);
	}

	return (0);
}
