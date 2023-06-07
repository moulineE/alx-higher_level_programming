#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the linked list
 * @number: the value to insert
 *
 * Return: he address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	current = *head;
	if (head == NULL)
	{
		return (NULL);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while ((current->next->n < number) && current->next != NULL && current != NULL)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
