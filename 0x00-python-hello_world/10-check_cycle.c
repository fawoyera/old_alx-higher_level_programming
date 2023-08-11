#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *search;
	int i = 0, j;

	temp = list;
	while (temp)
	{
		if (temp->next == list)
			return (1);

		search = list->next;
		for (j = 0; j < i; j++)
		{
			if (temp->next == search)
				return (1);
			search = search->next;
		}
		i++;

		temp = temp->next;
	}

	return (0);
}
