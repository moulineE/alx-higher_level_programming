#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly linked list
 * is a palindrome
 * @head: pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reader = *head;
	int y, count = 0, *pal_array, i = 0;

	if (*head == NULL)
		return (1);
	while (reader != NULL)
	{
		count++;
		reader = reader->next;

	}
	pal_array = malloc(count * sizeof(int));
	reader = *head;
	while (reader != NULL)
	{
		pal_array[i] = reader->n;
		reader = reader->next;
		if ((count % 2 == 0) && (i == (count / 2) - 1) && count > 2)
		{
			if (!(reader->n == reader->next->n))
			{
				free(pal_array);
				return (0);
			}
		}
		i++;
	}
	i = i - 1;
	for (y = 0; y < i; i--)
	{
		if (pal_array[i] != pal_array[y])
		{
			free(pal_array);
			return (0);
		}
		y++;
	}
	free(pal_array);
	return (1);
}
