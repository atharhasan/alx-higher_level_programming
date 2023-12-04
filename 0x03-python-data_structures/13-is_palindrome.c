#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - is_palindrome
 * @head: Pointer
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp, *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	while (prev != NULL && second_half != NULL)
	{
		if (prev->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		second_half = second_half->next;
	}
	prev = NULL;
	while (slow != NULL)
	{
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	*head = prev;
	return (is_palindrome);
}