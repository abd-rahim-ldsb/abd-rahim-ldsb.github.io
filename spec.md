# Landasan Digital Sdn. Bhd. - Landing Page Specification

## Project Context
Premium B2B landing page for Malaysian IT solutions company specializing in cybersecurity, cloud computing, and network infrastructure. Target audience: Enterprise clients seeking trusted IT partners.

## Hero Section (Video-First)
- **Style**: Cinematic muted autoplay loop video showcasing abstract digital/technology visuals
- **Color tone**: Deep red and black with digital particle effects
- **Overlay**: Semi-transparent gradient for text readability
- **Typography**: Massive headline "Your Success Begins With Us"
- **CTA**: Primary red button "Get Started" + Secondary ghost button "Our Solutions"

## Tech Strategy
- **Stack**: Single HTML file with embedded CSS and vanilla JavaScript
- **Animation**: CSS animations + Intersection Observer for scroll-triggered effects
- **No external frameworks** - Pure CSS Grid/Flexbox for layout

## Design System

### Color Palette (NO BLUE/PURPLE)
- **Primary Red**: #C8102E (Landasan brand red)
- **Deep Red**: #8B0000 (accent/hover states)
- **Black**: #0A0A0A (backgrounds, text)
- **Charcoal**: #1A1A1A (card backgrounds)
- **Grey**: #6B7280 (secondary text)
- **Light Grey**: #F3F4F6 (section backgrounds)
- **White**: #FFFFFF (text on dark, backgrounds)

### Typography
- **Headings**: Inter or system sans-serif, bold weights
- **Body**: Inter, regular weight
- **Scale**:
  - Hero: 4rem-6rem
  - H2: 2.5rem-3rem
  - H3: 1.5rem
  - Body: 1rem-1.125rem

### Layout
- **Max-width**: 1280px container
- **Grid**: 12-column responsive grid
- **Spacing**: 8px base unit (multiples: 16, 24, 32, 48, 64, 96px)

## Section Breakdown

1. **Navigation**: Fixed, transparent on hero, solid on scroll
2. **Hero**: Full viewport, video background, floating headline
3. **About/Why Choose Us**: 3-column feature cards
4. **Services**: Interactive cards with hover animations
5. **Solutions**: Tabbed or accordion interface with icons
6. **Stats Counter**: Animated numbers on scroll
7. **Technology Partners**: Logo carousel/grid
8. **Contact**: Form + company details + map placeholder
9. **Footer**: Links, contact info, social icons

## Animation Strategy
- Fade-in-up on scroll for sections
- Counter animation for stats
- Hover scale/shadow on cards
- Smooth scroll behavior
- Subtle parallax on hero elements
