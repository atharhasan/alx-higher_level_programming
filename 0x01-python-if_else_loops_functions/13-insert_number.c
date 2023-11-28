#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert_node
 * @head: Pointer
 * @number: number
 * Return: 1
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *curr, *prev;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	curr = *head;
	while (curr != NULL && curr->n <= number)
	{
		prev = curr;
		curr = curr->next;
	}

	prev->next = node;
	node->next = curr;

	return (node);
}
