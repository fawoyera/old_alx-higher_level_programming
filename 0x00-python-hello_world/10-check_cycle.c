#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle(loop) in it
 * @list: pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lag, *lead;

	lag = list;
	lead = list;
	while (lag && lead && lead->next)
	{
		lag = lag->next;
		lead = lead->next->next;
		if (lag == lead)
			return (1);
	}

	return (0);
}
