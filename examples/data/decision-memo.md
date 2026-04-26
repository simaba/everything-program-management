---
decision_id: DM-0001
title: Confirm fallback scope for supplier API delay
status: decided
owner: Sima Bagheri
decision_date: 2026-04-26
review_date: 2026-05-10
recommended_option: Option B
sponsor: Product Steering
linked_raid_ids:
  - R-0001
tags:
  - steering
  - supplier
  - dependency
---

# Decision memo

## Recommendation
Choose **Option B** and approve a narrowed fallback scope now so the steering package can proceed even if the supplier API remains partially unresolved.

## Options considered
- **Option A**: wait for full supplier confirmation before freezing scope
- **Option B**: approve fallback scope now and close remaining supplier gaps in parallel

## Rationale
Option B preserves decision velocity, reduces exposure to a single external dependency, and keeps milestone planning credible.

## Risks
Fallback scope may require one follow-on adjustment after supplier confirmation.

## Next actions
- confirm fallback boundary with engineering
- socialize the decision in the steering preread
- review supplier status at the next checkpoint
