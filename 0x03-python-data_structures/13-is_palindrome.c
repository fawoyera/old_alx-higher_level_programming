#include "lists.h"
int len_linked_list(listint_t *head);
int val_linked_list(listint_t *head, int index);

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to the linked list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j, length;

	if (*head == NULL)
		return (1);

	length = len_linked_list(*head);
	for (i = 0, j = length - 1; i < length / 2 + 1; i++, j--)
	{
		if (val_linked_list(*head, i) != val_linked_list(*head, j))
			return (0);
	}

	return (1);
}

/**
 * len_linked_list - find the length of a linked list
 * @head: pointer to the first node of the linked list
 *
 * Return: length of the list
 */
int len_linked_list(listint_t *head)
{
	int i = 0;
	listint_t *temp;

	temp = head;
	while (temp)
	{
		i++;
		temp = temp->next;
	}
	return (i);
}

/**
 * val_linked_list - return the value at given index of linked list
 * @head: pointer to first node of linked list
 * @index: index of node to fetch
 *
 * Return: value of node at given index
 */
int val_linked_list(listint_t *head, int index)
{
	int i = 0;
	listint_t *temp;

	temp = head;
	while (temp)
	{
		if (i == index)
			return (temp->n);
		temp = temp->next;
		i++;
	}
	return (0);
}
