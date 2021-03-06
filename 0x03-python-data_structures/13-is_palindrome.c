#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - a fun that determine if singly linked list is palindrome
 * @head: represents a pointer to head of singly linked list
 * Return: the value 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int size = 0, i = 0;
	int data[10240];

	if (head == NULL) /* For when non-existing list is not */
		return (0);

	if (*head == NULL) /*represents when empty list is palindrome */
		return (1);

	while (tmp) /*is used to find size of linked list */
	{
		tmp = tmp->next;
		size += 1;
	}
	if (size == 1) /* we chech if single node list is palindrome */
		return (1);

	tmp = *head;
	while (tmp) /*here we pull node data into array to compare */
	{
		data[i++] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i <= (size / 2); i++)
	{
		if (data[i] != data[size - i - 1])
			return (0);
	}
	return (1);
}
