# v2 persistence + DRF + receipt preservation pattern (Oct 12 2026)

Class: pizza_palace billing → v2 persistence + DRF REST + receipt preservation.

Key patterns verified in session:
- Django ORM persistence (models + migrations) coexisting with v1 in-memory
- Receipt format must match v1 screenshot (KES currency, Subtotal/TAX/Total lines)
- Persist receipt_text on Order; GET returns stored receipt
- DRF router must be wired (DefaultRouter + include in urlpatterns) or endpoints unreachable
- Postman collection (v2-only) + web client wired to /orders/ required before marking complete
- Two-axis code review (standards + spec) with parallel sub-agents
- Grilling + domain-modeling before spec; tickets with blocking edges
- Screenshot/reference capture when visual verification needed (`.scratch/billing/receipt_capture.md`)

Note overlap: only `applyflow-product-engine-patterns` covers this class; `grill-with-docs` and `domain-modeling` govern the design documentation layer. No consolidation needed.
