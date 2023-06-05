#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list to checks for a cycle
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	int sn = 0, cn = 0;
	listint_t *source = list;
	listint_t *checker = list;

	if (!list)
	{
		return (0);
	}
	while (source->next != NULL)
	{
		if ((source == checker) && (sn != cn))
		{
			return (1);
		}
		else if (checker->next != NULL)
		{
			checker = checker->next;
			cn = cn + 1;
			continue;
		}
		else
		{
			source = source->next;
			checker = list;
			sn = sn + 1;
			cn = 0;
			continue;
		}
	}
	return (0);
}
