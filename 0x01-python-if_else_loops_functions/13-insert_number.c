#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - Inserts number into  sorted singly-linked list
 * @head: A pointer the head of the linked list
 * @number: number to insert
 * Return: If the function fails - NULL
 *         else, a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
