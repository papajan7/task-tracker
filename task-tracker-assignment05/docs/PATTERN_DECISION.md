# Focused Pattern Decision

## Concrete maintainability problem

The baseline `TaskService.list_tasks` selected sort behavior with multiple conditional branches (`id`, `title`, `status`). Every additional ordering option would require editing this method, mixing selection logic and each sorting algorithm.

## Decision: apply Strategy once

The final version introduces the `TaskSortStrategy` protocol and two implementations in `app/strategies.py`:

- `CreatedAtStrategy` orders by creation timestamp and ID.
- `PriorityStatusStrategy` orders in-progress tasks, then todo tasks, then done tasks.

`TaskService.list_tasks` accepts a strategy object and delegates ordering to it. The CLI chooses the priority strategy for the `list` command.

## Before / after

- Before: one service method owned task retrieval and conditional sorting branches.
- After: service owns retrieval; strategy objects own ordering algorithms.

## Verification

`test_priority_strategy_orders_active_tasks_first` verifies both strategy outputs. The full test suite also checks that core task behavior remains intact.

## Trade-off

This is a small educational example with only two strategies. If no additional sort modes are expected, the abstraction may be more structure than the application needs. No other design pattern was introduced.
