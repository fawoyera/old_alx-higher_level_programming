#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to the linked list
 * @number: the number to insert
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp)
	{
		if (number > temp->n && number <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else if (temp->next)
		{
			temp = temp->next;
		}
		else
		{
			new->next = NULL;
			temp->next = new;
			return (new);
		}
	}
	new->next = NULL;
	*head = new;
	return (new);
}
