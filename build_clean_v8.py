import os

def build_v8():
    with open('index.html.bak', 'r') as f:
        src = f.read()

    # 1. Head part
    b_start = src.find('<body')
    b_end = src.find('>', b_start) + 1
    head_part = src[:b_end]

    # Additional CSS for Why Us, Pricing, and Mobile Sliders
    additional_css = """
    /* ==========================================================
       SECTION: WHY CREATORS CHOOSE US (6 CORE GUARANTEES)
       ========================================================== */
    .why-section {
      padding: 110px 0;
      position: relative;
      border-top: 1px solid rgba(255, 253, 217, 0.08);
      border-bottom: 1px solid rgba(255, 253, 217, 0.08);
      background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(224, 83, 38, 0.06) 0%, transparent 70%);
      overflow: hidden;
    }
    .why-card {
      background: rgba(20, 19, 19, 0.78);
      border: 1px solid rgba(255, 253, 217, 0.1);
      border-radius: 20px;
      padding: 32px 28px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: inset 0 1px 1.5px rgba(255, 255, 255, 0.08), 0 20px 40px -10px rgba(0, 0, 0, 0.7);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .why-card:hover {
      transform: translateY(-5px);
      border-color: rgba(224, 83, 38, 0.45);
      box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.2), 0 28px 60px -12px rgba(0, 0, 0, 0.9), 0 0 25px rgba(224, 83, 38, 0.12);
    }
    .why-icon-shell {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(224, 83, 38, 0.12);
      border: 1px solid rgba(224, 83, 38, 0.35);
      color: #e05326;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 800;
    }

    /* ==========================================================
       SECTION: TRANSPARENT PRICING PACKAGES
       ========================================================== */
    .pricing-section {
      padding: 120px 0;
      position: relative;
      border-top: 1px solid rgba(255, 253, 217, 0.08);
      border-bottom: 1px solid rgba(255, 253, 217, 0.08);
      background: #08080c;
      overflow: hidden;
    }
    .pricing-card {
      position: relative;
      background: rgba(20, 19, 19, 0.85);
      border: 1px solid rgba(255, 253, 217, 0.12);
      border-radius: 24px;
      padding: 38px 30px;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      box-shadow: inset 0 1px 1.5px rgba(255, 255, 255, 0.12), 0 24px 60px -15px rgba(0, 0, 0, 0.85);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .pricing-card:hover {
      transform: translateY(-6px);
      border-color: rgba(224, 83, 38, 0.45);
      box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.25), 0 32px 70px -15px rgba(0, 0, 0, 0.95), 0 0 35px rgba(224, 83, 38, 0.18);
    }
    .pricing-card.is-popular {
      background: rgba(24, 22, 22, 0.95);
      border: 1.5px solid rgba(224, 83, 38, 0.7);
      box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.25), 0 30px 70px -15px rgba(0, 0, 0, 0.95), 0 0 40px rgba(224, 83, 38, 0.25);
    }
    .pricing-card.is-popular:hover {
      border-color: #e05326;
      box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.3), 0 36px 80px -15px rgba(0, 0, 0, 0.98), 0 0 50px rgba(224, 83, 38, 0.35);
    }
    .pricing-popular-badge {
      position: absolute;
      top: -14px;
      left: 50%;
      transform: translateX(-50%);
      background: linear-gradient(135deg, #e05326 0%, #ff7744 100%);
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 16px;
      border-radius: 9999px;
      box-shadow: 0 4px 14px rgba(224, 83, 38, 0.5);
      white-space: nowrap;
    }
    .pricing-feature-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 13.5px;
      color: rgba(255, 253, 217, 0.85);
      line-height: 1.45;
    }
    .pricing-check-icon {
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: rgba(224, 83, 38, 0.18);
      border: 1px solid rgba(224, 83, 38, 0.45);
      color: #e05326;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1.5px;
    }
    .pricing-check-icon svg {
      width: 10px;
      height: 10px;
    }
    .pricing-guarantee-card {
      background: rgba(20, 19, 19, 0.6);
      border: 1px solid rgba(255, 253, 217, 0.08);
      border-radius: 16px;
      padding: 22px 20px;
      transition: all 0.25s ease;
    }
    .pricing-guarantee-card:hover {
      background: rgba(20, 19, 19, 0.85);
      border-color: rgba(224, 83, 38, 0.35);
      transform: translateY(-2px);
    }

    /* Mobile Multi-Column Sliders for Why Us & Pricing */
    @media (max-width: 1023px) {
      .why-cards-track,
      .pricing-cards-track {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        position: relative !important;
        height: auto !important;
        gap: 16px !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        scroll-snap-type: x mandatory !important;
        -webkit-overflow-scrolling: touch;
        width: 100vw !important;
        max-width: 100vw !important;
        margin-left: calc(-50vw + 50%) !important;
        padding: 8px 20px 20px !important;
        scroll-padding-left: 20px !important;
        scroll-padding-right: 20px !important;
        scrollbar-width: none;
      }
      .why-cards-track::-webkit-scrollbar,
      .pricing-cards-track::-webkit-scrollbar {
        display: none;
      }
      .why-cards-track > div,
      .pricing-cards-track > div {
        flex: 0 0 calc(100vw - 48px) !important;
        min-width: calc(100vw - 48px) !important;
        max-width: 420px !important;
        width: calc(100vw - 48px) !important;
        flex-shrink: 0 !important;
        margin-bottom: 0 !important;
        scroll-snap-align: start !important;
        box-sizing: border-box !important;
      }
    }
"""

    style_close = head_part.rfind('</style>')
    if style_close != -1:
        head_part = head_part[:style_close] + additional_css + '\n  ' + head_part[style_close:]

    # 2. Extract Work section
    w_start = src.find('<section id="work"')
    w_end = src.find('</section>', w_start) + len('</section>')
    work_html = src[w_start:w_end]

    # 3. Extract Modals
    m_start = src.find('<!-- QUICK VIEW PROJECT CASE STUDY MODAL -->')
    s_start = src.find('<!-- SCRIPT LOGIC -->')
    modals_html = src[m_start:s_start].strip()

    # 4. Extract JS Logic
    js_raw = src[s_start:]

    # Replace Diagnostic JS block with pricing mode switcher
    diag_start_marker = '/* ==========================================================\n       5. PROPRIETARY DIAGNOSTIC: LIVE SVG RETENTION LAB'
    diag_end_marker = '/* ==========================================================\n       6B. ZERO-FRICTION ONBOARDING'
    
    d1 = js_raw.find(diag_start_marker)
    d2 = js_raw.find(diag_end_marker)
    if d1 != -1 and d2 != -1:
        pricing_js = """/* ==========================================================
       5. TRANSPARENT PRICING TOGGLE SWITCHER
       ========================================================== */
    function setPricingMode(mode) {
      const btnMonthly = document.getElementById("pricing-tab-monthly");
      const btnPackages = document.getElementById("pricing-tab-packages");
      const pExplore = document.getElementById("price-explore");
      const pTrending = document.getElementById("price-trending");
      const pViral = document.getElementById("price-viral");
      const perExplore = document.getElementById("period-explore");
      const perTrending = document.getElementById("period-trending");
      const perViral = document.getElementById("period-viral");

      if (mode === "packages") {
        if (btnMonthly) {
          btnMonthly.classList.remove("bg-[#e05326]", "text-white");
          btnMonthly.classList.add("text-[rgba(255,253,217,0.7)]");
        }
        if (btnPackages) {
          btnPackages.classList.add("bg-[#e05326]", "text-white");
          btnPackages.classList.remove("text-[rgba(255,253,217,0.7)]");
        }
        if (pExplore) pExplore.textContent = "$327";
        if (pTrending) pTrending.textContent = "$305";
        if (pViral) pViral.textContent = "$278";
        if (perExplore) perExplore.textContent = "/ per video";
        if (perTrending) perTrending.textContent = "/ per video";
        if (perViral) perViral.textContent = "/ per video";
        playBeep(580, "sine", 0.04);
      } else {
        if (btnPackages) {
          btnPackages.classList.remove("bg-[#e05326]", "text-white");
          btnPackages.classList.add("text-[rgba(255,253,217,0.7)]");
        }
        if (btnMonthly) {
          btnMonthly.classList.add("bg-[#e05326]", "text-white");
          btnMonthly.classList.remove("text-[rgba(255,253,217,0.7)]");
        }
        if (pExplore) pExplore.textContent = "$1,495";
        if (pTrending) pTrending.textContent = "$2,795";
        if (pViral) pViral.textContent = "$4,495";
        if (perExplore) perExplore.textContent = "/ month";
        if (perTrending) perTrending.textContent = "/ month";
        if (perViral) perViral.textContent = "/ month";
        playBeep(480, "sine", 0.04);
      }
    }
    window.setPricingMode = setPricingMode;

    """
        js_raw = js_raw[:d1] + pricing_js + js_raw[d2:]

    # Remove Director JS
    dir_start_marker = '/* ==========================================================\n       6C. STUDIO DIRECTOR & INFRASTRUCTURE'
    dir_end_marker = '/* ==========================================================\n       REVERSIBLE SCROLL-TRIGGERED ANIMATIONS'
    dir1 = js_raw.find(dir_start_marker)
    dir2 = js_raw.find(dir_end_marker)
    if dir1 != -1 and dir2 != -1:
        js_raw = js_raw[:dir1] + js_raw[dir2:]

    # Update mobile sliders in JS
    js_raw = js_raw.replace(
        'initMobileTouchSlider(".director-cards-track", "director-carousel-dots", "director-card-counter", ".director-cards-track > div");',
        'initMobileTouchSlider(".why-cards-track", "why-carousel-dots", "why-card-counter", ".why-cards-track > div");\n    initMobileTouchSlider(".pricing-cards-track", "pricing-carousel-dots", "pricing-card-counter", ".pricing-cards-track > div");'
    )

    # 5. Core HTML structure
    body_html = f"""
  <!-- Ambient Backdrop Glow -->
  <div class="hero-glow"></div>

  <!-- Dynamic Floating & Condensed Header on Scroll with Active Reading Progress Bar -->
  <header id="site-header">
    <div class="site-header-inner">
      
      <!-- Brand Logo -->
      <a href="#hero" class="header-logo flex items-center tracking-tight text-white font-extrabold text-[1.15rem] uppercase font-['Plus_Jakarta_Sans',sans-serif] hover:opacity-95 transition-opacity flex-shrink-0">
        <span class="tracking-[-0.03em] text-[#FFFDD9]">PSYCHED<span class="text-[#e05326] font-black">.</span>STUDIO</span>
      </a>

      <!-- Clean Minimal Nav Links -->
      <nav class="header-nav hidden md:flex items-center gap-5 lg:gap-7">
        <a href="#services" class="clean-nav-link">Services</a>
        <a href="#why-us" class="clean-nav-link">Why Us</a>
        <a href="#how-it-works" class="clean-nav-link">How It Works</a>
        <a href="#work" class="clean-nav-link">Work &amp; Proof</a>
        <a href="#pricing" class="clean-nav-link">Pricing</a>
        <a href="#faq" class="clean-nav-link">FAQ</a>
        <a href="#booking" class="clean-nav-link text-[#e05326]">Book a Call</a>
      </nav>

      <!-- Right CTAs & Badges -->
      <div class="header-right-actions">
        <!-- Audio Haptic Sound Toggle -->
        <button id="audio-toggle-btn" class="header-audio-btn" type="button" aria-label="Toggle Sound Effects" title="Toggle Sound FX">
          <span class="audio-waves" aria-hidden="true">
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
          </span>
          <span id="audio-toggle-label" class="hidden lg:inline text-[11px] font-mono font-bold tracking-wider">AUDIO ON</span>
        </button>

        <!-- Availability Status Pill -->
        <span class="header-status-pill hidden sm:inline-flex">
          <span class="w-2 h-2 rounded-full bg-[#e05326] animate-pulse"></span>
          <span>2 SPOTS OPEN</span>
        </span>

        <!-- Book Project Pill Button -->
        <a href="#booking" class="header-cta-btn">
          Get Started
        </a>
      </div>

      <!-- Active Scroll Reading Progress Bar Running Directly Under Header -->
      <div class="header-progress-track">
        <div id="header-progress-bar" class="header-progress-fill"></div>
      </div>

    </div>
  </header>

  <!-- ==========================================================================
       SECTION 1: HERO (High-Yield Telemetry 3D Canvas + Crystal-Clear Value Proposition)
       ========================================================================== -->
  <section id="hero" class="relative min-h-[90vh] pt-32 pb-24 flex flex-col items-center justify-center px-6 overflow-hidden">
    
    <!-- Interactive High-Yield Growth & Revenue Telemetry Canvas -->
    <div id="hero-canvas-container" class="absolute inset-0 pointer-events-auto z-0 opacity-80 transition-opacity duration-700 overflow-hidden">
      <canvas id="hero-3d-canvas" class="w-full h-full block"></canvas>
    </div>

    <!-- Realtime Interactive Graph HUD (Pops up on graph interaction & auto-hides) -->
    <div id="hero-chart-hud" class="pointer-events-none absolute top-28 right-6 lg:right-12 z-20 hidden md:flex items-center gap-3 sm:gap-4 px-5 py-2.5 rounded-full bg-[rgba(16,17,23,0.88)] border border-[rgba(255,253,217,0.16)] backdrop-blur-xl font-mono text-xs sm:text-[13px] shadow-2xl transition-all duration-300 opacity-0 translate-y-2">
      <div class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-[#e05326] animate-pulse"></span>
        <span class="text-[rgba(255,253,217,0.6)]">TRAJECTORY •</span>
        <span id="hud-day" class="text-white font-bold tracking-wider">DAY 77</span>
      </div>
      <div class="hidden sm:block h-3.5 w-px bg-white/15"></div>
      <div class="flex items-center gap-1.5">
        <span class="text-[#e05326] font-bold">VIEWS:</span>
        <span id="hud-views" class="text-[#FFFDD9] font-bold tracking-wider">10.8M</span>
      </div>
      <div class="hidden sm:block h-3.5 w-px bg-white/15"></div>
      <div class="flex items-center gap-1.5">
        <span class="text-[#e05326] font-bold">REVENUE:</span>
        <span id="hud-revenue" class="text-[#FFFDD9] font-bold tracking-wider">+$178K/mo</span>
      </div>
      <div class="hidden md:block h-3.5 w-px bg-white/15"></div>
      <div class="hidden md:flex items-center gap-1.5">
        <span class="text-[#FFFDD9]/60">SLA:</span>
        <span class="text-[#FFFDD9] font-bold">48H SPRINT</span>
      </div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center">
      
      <!-- Studio Trust Badge -->
      <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-[#181616]/90 border border-[rgba(255,253,217,0.14)] backdrop-blur-md text-xs sm:text-[13px] font-mono font-bold text-[#FFFDD9] mb-8 shadow-xl">
        <span class="w-2 h-2 rounded-full bg-[#e05326] animate-ping"></span>
        <span class="text-[#e05326]">★</span>
        <span>#1 VIDEO EDITING &amp; YOUTUBE CHANNEL MANAGEMENT STUDIO</span>
      </div>

      <!-- Main High-Converting Headline -->
      <h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-[76px] font-extrabold tracking-tight text-[#FFFDD9] uppercase max-w-5xl leading-[1.04]">
        World-Class Video Editing. <span class="font-serif italic font-normal text-[#e05326]">Zero Channel Stress.</span>
      </h1>

      <!-- Subtitle Focused on Reclaiming 20+ Hours & Predictable Turnaround -->
      <p class="mt-6 text-base sm:text-lg md:text-xl text-[rgba(255,253,217,0.85)] max-w-3xl font-normal leading-relaxed text-balance">
        Reclaim 20+ hours every week. We turn raw footage into viral long-form mastercuts, short-form reels, and custom high-CTR thumbnails. Guaranteed 48-hour turnarounds. Unlimited revisions. Dedicated editor.
      </p>

      <!-- Action Triggers -->
      <div class="pointer-events-auto mt-8 sm:mt-10 flex flex-wrap items-center justify-center gap-4">
        <!-- Primary Button: View Pricing & Packages -->
        <a href="#pricing" class="hero-primary-cta">
          <span>View Pricing &amp; Packages</span>
          <svg class="w-4 h-4 text-[#FFFDD9]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>

        <!-- Secondary Button: Book Discovery Call -->
        <a href="#booking" class="inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-[#181616]/90 hover:bg-[#222020] text-[#FFFDD9] text-sm font-semibold border border-white/10 backdrop-blur-md transition-all hover:scale-105 active:scale-95 shadow-lg group">
          <span>Book Discovery Call</span>
          <span class="text-[#e05326] font-bold">→</span>
        </a>

        <!-- Showreel Trigger Button -->
        <button id="trigger-showreel" type="button" class="inline-flex items-center gap-2 px-5 py-3 rounded-full bg-white/[0.04] hover:bg-white/[0.08] text-[rgba(255,253,217,0.7)] hover:text-white text-xs font-mono border border-white/[0.08] transition-all">
          <svg class="w-3.5 h-3.5 text-[#e05326]" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          <span>Watch Reel (0:58)</span>
        </button>
      </div>

      <!-- Real Anchor Metrics Ribbon -->
      <div class="pointer-events-auto mt-12 grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-6 w-full max-w-4xl px-4 hero-metrics-track">
        <div class="hero-metric-card p-4 rounded-2xl bg-[#181616]/80 border border-white/[0.08] backdrop-blur-md text-center hover:border-[#e05326]/40 transition-all">
          <div class="hero-stat-val text-2xl sm:text-3xl font-bold text-[#FFFDD9] tracking-tight font-mono" data-target="140" data-prefix="" data-suffix="M+" data-decimals="0">140M+</div>
          <div class="text-xs text-[rgba(255,253,217,0.6)] mt-1">Organic Views Generated</div>
        </div>
        <div class="hero-metric-card p-4 rounded-2xl bg-[#181616]/80 border border-white/[0.08] backdrop-blur-md text-center hover:border-[#e05326]/40 transition-all">
          <div class="hero-stat-val text-2xl sm:text-3xl font-bold text-[#FFFDD9] tracking-tight font-mono" data-target="48" data-prefix="" data-suffix=" Hours" data-decimals="0">48 Hours</div>
          <div class="text-xs text-[rgba(255,253,217,0.6)] mt-1">Guaranteed First Draft Delivery</div>
        </div>
        <div class="hero-metric-card p-4 rounded-2xl bg-[#181616]/80 border border-white/[0.08] backdrop-blur-md text-center hover:border-[#e05326]/40 transition-all">
          <div class="hero-stat-val text-2xl sm:text-3xl font-bold text-[#FFFDD9] tracking-tight font-mono" data-target="20" data-prefix="" data-suffix="+ Hrs" data-decimals="0">20+ Hrs</div>
          <div class="text-xs text-[rgba(255,253,217,0.6)] mt-1">Saved Per Creator Every Week</div>
        </div>
        <div class="hero-metric-card p-4 rounded-2xl bg-[#181616]/80 border border-white/[0.08] backdrop-blur-md text-center hover:border-[#e05326]/40 transition-all">
          <div class="text-2xl sm:text-3xl font-bold text-[#FFFDD9] tracking-tight font-mono">4.9 ★★★★★</div>
          <div class="text-xs text-[rgba(255,253,217,0.6)] mt-1">Top-Rated Creator Reviews</div>
        </div>
      </div>

      <!-- Mobile Hero Metrics Slider Dots Indicator -->
      <div class="pointer-events-auto flex items-center justify-center gap-1.5 mt-2 md:hidden" id="hero-metrics-dots">
        <button class="slider-dot active" data-index="0" aria-label="Metric 1"></button>
        <button class="slider-dot" data-index="1" aria-label="Metric 2"></button>
        <button class="slider-dot" data-index="2" aria-label="Metric 3"></button>
        <button class="slider-dot" data-index="3" aria-label="Metric 4"></button>
      </div>

      <!-- Sub-Banner Callout -->
      <div class="pointer-events-auto mt-6 max-w-3xl mx-4 px-6 py-4 rounded-2xl bg-[rgba(16,17,23,0.85)] border border-[rgba(255,253,217,0.1)] backdrop-blur-md text-xs sm:text-[13px] text-[rgba(255,253,217,0.8)] font-mono leading-relaxed text-center sm:text-left flex flex-col sm:flex-row items-center gap-3.5 shadow-xl">
        <div class="flex items-center gap-2 text-[#e05326] font-bold uppercase tracking-wider flex-shrink-0">
          <span class="w-2 h-2 rounded-full bg-[#e05326] animate-pulse"></span>
          <span>WHAT WE HANDLE:</span>
        </div>
        <div>
          Every order includes custom motion graphics, sound design, color correction, and unlimited revisions. You hit record; we build your compounding media machine.
        </div>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 2: DUAL ANGLED VELOCITY TICKER (Opposite Directions & Scroll-Responsive)
       ========================================================================== -->
  <div id="stats" class="psy-velocity-band" aria-hidden="true">
    <!-- Top Strip: Solid High-Impact Rusty Orange Ribbon (Angled -2.2deg, moves left) -->
    <div class="psy-band-strip">
      <div class="psy-band-row" data-dir="-1">
        <span>48-HOUR FIRST DRAFT GUARANTEE ✦ UNLIMITED REVISIONS ✦ DEDICATED VIDEO EDITOR ✦ MOTION GRAPHICS &amp; SOUND DESIGN ✦ FULL YOUTUBE CHANNEL MANAGEMENT ✦ CUSTOM HIGH-CTR THUMBNAILS ✦</span>
        <span>48-HOUR FIRST DRAFT GUARANTEE ✦ UNLIMITED REVISIONS ✦ DEDICATED VIDEO EDITOR ✦ MOTION GRAPHICS &amp; SOUND DESIGN ✦ FULL YOUTUBE CHANNEL MANAGEMENT ✦ CUSTOM HIGH-CTR THUMBNAILS ✦</span>
        <span>48-HOUR FIRST DRAFT GUARANTEE ✦ UNLIMITED REVISIONS ✦ DEDICATED VIDEO EDITOR ✦ MOTION GRAPHICS &amp; SOUND DESIGN ✦ FULL YOUTUBE CHANNEL MANAGEMENT ✦ CUSTOM HIGH-CTR THUMBNAILS ✦</span>
        <span>48-HOUR FIRST DRAFT GUARANTEE ✦ UNLIMITED REVISIONS ✦ DEDICATED VIDEO EDITOR ✦ MOTION GRAPHICS &amp; SOUND DESIGN ✦ FULL YOUTUBE CHANNEL MANAGEMENT ✦ CUSTOM HIGH-CTR THUMBNAILS ✦</span>
      </div>
    </div>
    <!-- Bottom Strip: Sleek Ghost Outline Ribbon Coming Underneath (Angled +1.8deg, moves right) -->
    <div class="psy-band-ghost">
      <div class="psy-band-row" data-dir="1">
        <span>+240% AVERAGE WATCH TIME ✦ 140M+ ORGANIC VIEWS GENERATED ✦ PREMIERE &amp; AFTER EFFECTS EXPERTS ✦ ZERO FREELANCER DRAG ✦ TURNKEY POST-PRODUCTION ✦ RECLAIM 20+ HOURS/WEEK ✦</span>
        <span>+240% AVERAGE WATCH TIME ✦ 140M+ ORGANIC VIEWS GENERATED ✦ PREMIERE &amp; AFTER EFFECTS EXPERTS ✦ ZERO FREELANCER DRAG ✦ TURNKEY POST-PRODUCTION ✦ RECLAIM 20+ HOURS/WEEK ✦</span>
        <span>+240% AVERAGE WATCH TIME ✦ 140M+ ORGANIC VIEWS GENERATED ✦ PREMIERE &amp; AFTER EFFECTS EXPERTS ✦ ZERO FREELANCER DRAG ✦ TURNKEY POST-PRODUCTION ✦ RECLAIM 20+ HOURS/WEEK ✦</span>
        <span>+240% AVERAGE WATCH TIME ✦ 140M+ ORGANIC VIEWS GENERATED ✦ PREMIERE &amp; AFTER EFFECTS EXPERTS ✦ ZERO FREELANCER DRAG ✦ TURNKEY POST-PRODUCTION ✦ RECLAIM 20+ HOURS/WEEK ✦</span>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       SECTION 3: CORE SERVICES (Sticky Two-Column & Matter.js Bursting Tag Physics)
       ========================================================================== -->
  <section id="services" class="services-sticky-section overflow-visible relative">
    <!-- Section-Wide Dynamic Backdrop Blur (Only Active When Hovering Pillars) -->
    <div class="services-bg-blur" aria-hidden="true"></div>

    <div class="max-w-7xl mx-auto px-6 relative z-10">
      
      <div class="sticky-two-col items-start">
        <!-- Sticky Left Title Column -->
        <div class="sticky-left-col">
          <span class="text-xs font-mono font-bold text-[#e05326] uppercase tracking-widest block mb-3">WHAT WE DO</span>
          <h2 class="text-4xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.05] mb-6">
            World-Class <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">Editing.</span>
          </h2>
          <p class="text-base sm:text-lg text-[rgba(255,253,217,0.7)] leading-relaxed mb-8 max-w-md">
            No bloated agency overhead or endless freelancer chasing. You work with a dedicated creative pod that edits, color corrects, sound masters, and packages your content on autopilot.
          </p>
          <a href="#pricing" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#FFFDD9] text-[#141313] text-xs font-extrabold uppercase tracking-wider shadow-[0_4px_20px_rgba(255,253,217,0.25)] hover:bg-white hover:scale-105 active:scale-95 transition-all">
            View Pricing &amp; Packages <span>→</span>
          </a>
        </div>

        <!-- Right Column: Kinetic Hover-Burst List -->
        <div class="hover-burst-list flex flex-col relative">
          
          <!-- Pillar 1: Long-Form Video Editing -->
          <div class="hover-burst-item pillar-red" data-pillar="0">
            <div class="burst-trigger-row group">
              <div class="flex items-center gap-4 sm:gap-6">
                <span class="text-sm sm:text-base font-mono font-bold text-[#e05326] tracking-wider">[01]</span>
                <div>
                  <h3 class="burst-title-text text-2xl sm:text-3xl lg:text-4xl font-extrabold uppercase tracking-tight text-[#FFFDD9] group-hover:text-[#e05326] transition-colors duration-300">
                    Long-Form Video Editing
                  </h3>
                  <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] mt-1 font-normal max-w-xl">
                    Horizontal videos for YouTube, podcasts, documentaries, and courses. Any style, any niche. We turn raw footage into high-retention stories with pattern interrupts and broadcast audio.
                  </p>
                </div>
              </div>
              <div class="burst-trigger-badge flex items-center gap-3">
                <span class="hidden sm:inline-block text-[11px] font-mono tracking-widest uppercase text-[rgba(255,253,217,0.4)] group-hover:text-[#e05326] transition-colors">Hover Tags</span>
                <div class="w-10 h-10 rounded-full border border-[rgba(255,253,217,0.15)] flex items-center justify-center text-[#FFFDD9] group-hover:bg-[#e05326] group-hover:border-[#e05326] group-hover:text-white transition-all duration-300">
                  <svg class="w-4 h-4 transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </div>
              </div>
            </div>

            <!-- Absolute Floating Stage (Matter.js Rigid-Body Tags) -->
            <div class="burst-floating-stage" aria-hidden="true">
              <div class="burst-pill-item pill-tag burst-pill-1">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#YouTubeLongForm</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-2">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#RetentionPacing</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-3">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#BroadcastAudioSFX</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-4">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#MotionGraphics</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-5">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#CinematicGrading</span>
              </div>
            </div>
            
            <div class="burst-item-divider"></div>
          </div>

          <!-- Pillar 2: Short-Form Video Editing -->
          <div class="hover-burst-item pillar-cream" data-pillar="1">
            <div class="burst-trigger-row group">
              <div class="flex items-center gap-4 sm:gap-6">
                <span class="text-sm sm:text-base font-mono font-bold text-[#FFFDD9] tracking-wider">[02]</span>
                <div>
                  <h3 class="burst-title-text text-2xl sm:text-3xl lg:text-4xl font-extrabold uppercase tracking-tight text-[#FFFDD9] group-hover:text-white transition-colors duration-300">
                    Short-Form Video Editing
                  </h3>
                  <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] mt-1 font-normal max-w-xl">
                    Attention-grabbing vertical videos for YouTube Shorts, Instagram Reels, and TikTok. Original content and long-form reformats with animated captions, kinetic b-roll, and trending sound design.
                  </p>
                </div>
              </div>
              <div class="burst-trigger-badge flex items-center gap-3">
                <span class="hidden sm:inline-block text-[11px] font-mono tracking-widest uppercase text-[rgba(255,253,217,0.4)] group-hover:text-[#FFFDD9] transition-colors">Hover Tags</span>
                <div class="w-10 h-10 rounded-full border border-[rgba(255,253,217,0.15)] flex items-center justify-center text-[#FFFDD9] group-hover:bg-[#FFFDD9] group-hover:border-[#FFFDD9] group-hover:text-[#181616] transition-all duration-300">
                  <svg class="w-4 h-4 transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </div>
              </div>
            </div>

            <!-- Absolute Floating Stage -->
            <div class="burst-floating-stage" aria-hidden="true">
              <div class="burst-pill-item pill-tag burst-pill-1">
                <span class="tag-dot bg-[#FFFDD9]"></span>
                <span class="tag-text">#YouTubeShorts</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-2">
                <span class="tag-dot bg-[#FFFDD9]"></span>
                <span class="tag-text">#InstagramReels</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-3">
                <span class="tag-dot bg-[#FFFDD9]"></span>
                <span class="tag-text">#TikTokAlgorithm</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-4">
                <span class="tag-dot bg-[#FFFDD9]"></span>
                <span class="tag-text">#AnimatedCaptions</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-5">
                <span class="tag-dot bg-[#FFFDD9]"></span>
                <span class="tag-text">#KineticHooks</span>
              </div>
            </div>

            <div class="burst-item-divider"></div>
          </div>

          <!-- Pillar 3: YouTube Channel Management -->
          <div class="hover-burst-item pillar-red" data-pillar="2">
            <div class="burst-trigger-row group">
              <div class="flex items-center gap-4 sm:gap-6">
                <span class="text-sm sm:text-base font-mono font-bold text-[#e05326] tracking-wider">[03]</span>
                <div>
                  <h3 class="burst-title-text text-2xl sm:text-3xl lg:text-4xl font-extrabold uppercase tracking-tight text-[#FFFDD9] group-hover:text-[#e05326] transition-colors duration-300">
                    YouTube Channel Management
                  </h3>
                  <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] mt-1 font-normal max-w-xl">
                    Our dedicated channel growth experts run and grow your YouTube channel. We design high-CTR thumbnails, write optimized titles, schedule uploads, structure chapters, and deliver weekly retention reports.
                  </p>
                </div>
              </div>
              <div class="burst-trigger-badge flex items-center gap-3">
                <span class="hidden sm:inline-block text-[11px] font-mono tracking-widest uppercase text-[rgba(255,253,217,0.4)] group-hover:text-[#e05326] transition-colors">Hover Tags</span>
                <div class="w-10 h-10 rounded-full border border-[rgba(255,253,217,0.15)] flex items-center justify-center text-[#FFFDD9] group-hover:bg-[#e05326] group-hover:border-[#e05326] group-hover:text-white transition-all duration-300">
                  <svg class="w-4 h-4 transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </div>
              </div>
            </div>

            <!-- Absolute Floating Stage -->
            <div class="burst-floating-stage" aria-hidden="true">
              <div class="burst-pill-item pill-tag burst-pill-1">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#HighCTRThumbnails</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-2">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#TitleTestingAB</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-3">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#YouTubeSEO</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-4">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#UploadScheduling</span>
              </div>
              <div class="burst-pill-item pill-tag burst-pill-5">
                <span class="tag-dot bg-[#e05326]"></span>
                <span class="tag-text">#RetentionAnalytics</span>
              </div>
            </div>

            <div class="burst-item-divider"></div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 4: WHY CREATORS CHOOSE US (6 Core Agency Guarantees - Replaces Messy Director Block)
       ========================================================================== -->
  <section id="why-us" class="why-section">
    <div class="max-w-7xl mx-auto px-6">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.3)] text-[#e05326] text-xs font-mono font-bold uppercase tracking-widest mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-[#e05326] animate-pulse"></span>
          WHAT WE HANDLE
        </div>
        <h2 class="text-4xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.08]">
          The Video Studio Built for <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">Creator Leverage.</span>
        </h2>
        <p class="text-[rgba(255,253,217,0.75)] text-base sm:text-lg mt-3 leading-relaxed">
          Every order includes motion graphics, sound design, color correction, and unlimited revisions. Here’s why top YouTubers, podcasters, and brands switch to Psyched Studio:
        </p>
      </div>

      <!-- 6 Guarantees Grid (Slider on Mobile, 3x2 on Desktop) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch why-cards-track" id="why-cards-track">
        
        <!-- Guarantee 1: Dedicated Team -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">01</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Dedicated Team &amp; Lead Editor
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              You work with the exact same creative pod on every video: your video manager, dedicated lead editor, thumbnail artist, and channel growth manager. No retraining strangers.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>CONSISTENT STYLE</span>
            <span>✦ ZERO RE-EXPLAINING</span>
          </div>
        </div>

        <!-- Guarantee 2: 48-Hour Turnaround -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">02</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Guaranteed 48-Hour Turnaround
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              We guarantee fast, reliable delivery on every video order—operating Monday through Saturday PST so your content calendar and sponsor commitments never miss a beat.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>48H FIRST DRAFT</span>
            <span>✦ MON-SAT SLA</span>
          </div>
        </div>

        <!-- Guarantee 3: Unlimited Revisions -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">03</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Unlimited Revisions
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              Say goodbye to lengthy revision cycles! Leave frame-accurate timecoded comments directly on your video drafts until you are 100% in love with the final cut.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>FRAME-ACCURATE</span>
            <span>✦ 100% SATISFACTION</span>
          </div>
        </div>

        <!-- Guarantee 4: Motion Graphics & Sound Design -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">04</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Motion Graphics &amp; Sound Included
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              Never get charged extra for essentials. Every order includes custom 2D/3D kinetic typography, branded lower-thirds, licensed SFX, and broadcast audio mastering.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>NO HIDDEN FEES</span>
            <span>✦ BROADCAST MASTER</span>
          </div>
        </div>

        <!-- Guarantee 5: Multiple Editors on Demand -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">05</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Multiple Editors at No Extra Cost
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              Scaling your output? We’re the only video editing studio that provides multiple vetted editors simultaneously at no surcharge so you can batch content seamlessly.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>BATCHING FRIENDLY</span>
            <span>✦ SCALE CAPACITY</span>
          </div>
        </div>

        <!-- Guarantee 6: Frictionless Client Portal -->
        <div class="why-card">
          <div>
            <div class="why-icon-shell">06</div>
            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2.5">
              Drag-and-Drop Client Dashboard
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.7)] leading-relaxed">
              Upload raw footage in seconds, receive automated status updates every 24 hours, and chat directly with your creative pod anytime in our hyper-efficient portal.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.08)] flex items-center justify-between text-xs font-mono text-[#e05326]">
            <span>24H PROGRESS UPDATES</span>
            <span>✦ DIRECT CHAT</span>
          </div>
        </div>

      </div>

      <!-- Mobile Why Us Slider Dots Indicator -->
      <div class="flex items-center justify-between mt-4 px-2 text-xs font-mono text-[rgba(255,253,217,0.65)] lg:hidden">
        <span class="inline-flex items-center gap-1.5 text-[#e05326] font-bold text-[11px]">
          <span class="inline-block animate-pulse">←</span> Swipe Guarantees <span class="inline-block animate-pulse">→</span>
        </span>
        <div class="flex items-center gap-1.5" id="why-carousel-dots">
          <button class="slider-dot active" data-index="0" aria-label="Guarantee 1"></button>
          <button class="slider-dot" data-index="1" aria-label="Guarantee 2"></button>
          <button class="slider-dot" data-index="2" aria-label="Guarantee 3"></button>
          <button class="slider-dot" data-index="3" aria-label="Guarantee 4"></button>
          <button class="slider-dot" data-index="4" aria-label="Guarantee 5"></button>
          <button class="slider-dot" data-index="5" aria-label="Guarantee 6"></button>
        </div>
        <span id="why-card-counter" class="font-bold tracking-wider text-[rgba(255,253,217,0.8)] text-[11px]">1 / 6</span>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 5: HOW IT WORKS (3-Step Frictionless Workflow)
       ========================================================================== -->
  <section id="how-it-works" class="deploy-process-section">
    <!-- Backwards compatible anchor for legacy scroll links -->
    <div id="process" style="position: absolute; top: 0;"></div>

    <div class="max-w-7xl mx-auto px-6">
      
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-16">
        <div>
          <span class="text-xs font-mono font-bold text-[#e05326] uppercase tracking-widest block mb-3">HOW IT WORKS</span>
          <h2 class="text-3xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.08]">
            <span class="deploy-headline-1 scroll-reveal">From Raw Footage to</span>
            <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326] deploy-headline-2 kinetic-deploy-title scroll-reveal mt-1 sm:mt-2 block" id="kinetic-deploy-steps">
              <span class="kinetic-word-mask"><span class="kinetic-word" style="--k-idx: 0">Channel</span></span>
              <span class="kinetic-word-mask"><span class="kinetic-word kinetic-word-highlight" style="--k-idx: 1">Domination.</span></span>
            </span>
          </h2>
        </div>
        <p class="text-[rgba(255,253,217,0.7)] text-sm sm:text-base max-w-lg leading-relaxed">
          Our creator-built workflow makes it easy to upload footage, review drafts, and collaborate with your team in one place.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8" id="deploy-cards-grid">
        
        <!-- Step 1: Upload Raw Footage -->
        <div class="deploy-step-card" data-step="1">
          <div>
            <div class="flex items-center justify-between gap-4 mb-6">
              <span class="deploy-step-num">01</span>
              <span class="px-2.5 py-1 rounded bg-[rgba(255,253,217,0.06)] border border-[rgba(255,253,217,0.12)] text-[10px] font-mono text-[#FFFDD9] font-bold uppercase">
                STEP 1: UPLOAD FOOTAGE
              </span>
            </div>
            <h3 class="text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-3">
              1. Upload Raw Footage
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] leading-relaxed mb-6">
              Drop your raw footage directly into your private dashboard or send a Google Drive / Dropbox link. Include your brief notes or let our creative team direct the retention vision.
            </p>
          </div>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.08)]">
            <span class="text-[11px] font-mono text-[#e05326] font-bold block mb-1 uppercase">YOUR INPUT:</span>
            <span class="text-xs text-[#FFFDD9] font-semibold">Zero Brief Friction • Secure Cloud Ingest</span>
          </div>
        </div>

        <!-- Step 2: 48-Hour Studio Edit -->
        <div class="deploy-step-card border-t-2 border-t-[#e05326]" data-step="2">
          <div>
            <div class="flex items-center justify-between gap-4 mb-6">
              <span class="deploy-step-num text-[#e05326]">02</span>
              <span class="px-2.5 py-1 rounded bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.35)] text-[10px] font-mono text-[#e05326] font-bold uppercase">
                STEP 2: 48H STUDIO SPRINT
              </span>
            </div>
            <h3 class="text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-3">
              2. 48-Hour Studio Edit
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] leading-relaxed mb-6">
              Your dedicated lead editor cuts dead air, patterns interrupts, grades color, mixes broadcast sound design, animates kinetic b-roll, and crafts custom high-CTR thumbnails.
            </p>
          </div>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.08)]">
            <span class="text-[11px] font-mono text-[#e05326] font-bold block mb-1 uppercase">OUR OUTPUT:</span>
            <span class="text-xs text-[#FFFDD9] font-semibold">48-Hour First Draft • Motion Graphics &amp; SFX</span>
          </div>
        </div>

        <!-- Step 3: Review & 1-Click Publish -->
        <div class="deploy-step-card" data-step="3">
          <div>
            <div class="flex items-center justify-between gap-4 mb-6">
              <span class="deploy-step-num">03</span>
              <span class="px-2.5 py-1 rounded bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.35)] text-[10px] font-mono text-[#e05326] font-bold uppercase tracking-wider">
                STEP 3: 1-CLICK PUBLISH
              </span>
            </div>
            <h3 class="text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-3">
              3. Review &amp; 1-Click Publish
            </h3>
            <p class="text-xs sm:text-sm text-[rgba(255,253,217,0.65)] leading-relaxed mb-6">
              Review your draft with frame-by-frame timecoded notes until you’re 100% satisfied. Download 4K masters directly or let us schedule and SEO-optimize the YouTube upload.
            </p>
          </div>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.08)]">
            <span class="text-[11px] font-mono text-[#e05326] font-bold block mb-1 uppercase">FINAL RESULT:</span>
            <span class="text-xs text-[#FFFDD9] font-semibold">Unlimited Revisions • Hands-Off Channel Growth</span>
          </div>
        </div>

      </div>

      <!-- Mobile Process Steps Slider Indicator Controls -->
      <div class="flex items-center justify-between mt-4 px-2 text-xs font-mono text-[rgba(255,253,217,0.65)] md:hidden">
        <span class="inline-flex items-center gap-1.5 text-[#e05326] font-bold text-[11px]">
          <span class="inline-block animate-pulse">←</span> Swipe Steps <span class="inline-block animate-pulse">→</span>
        </span>
        <div class="flex items-center gap-1.5" id="process-carousel-dots">
          <button class="slider-dot active" data-index="0" aria-label="Step 1"></button>
          <button class="slider-dot" data-index="1" aria-label="Step 2"></button>
          <button class="slider-dot" data-index="2" aria-label="Step 3"></button>
        </div>
        <span id="process-card-counter" class="font-bold tracking-wider text-[rgba(255,253,217,0.8)] text-[11px]">1 / 3</span>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 6: VERIFIED WORK & PROOF (High-Converting Video Showcase)
       ========================================================================== -->
  {work_html}

  <!-- ==========================================================================
       SECTION 7: TRANSPARENT PRICING PACKAGES (Tasty Edits Style High-Converting Funnel)
       ========================================================================== -->
  <section id="pricing" class="pricing-section">
    <div class="max-w-7xl mx-auto px-6">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.3)] text-[#e05326] text-xs font-mono font-bold uppercase tracking-widest mb-4">
          TRANSPARENT PRICING • NO CONTRACTS
        </div>
        <h2 class="text-4xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.06]">
          Predictable Flat Pricing. <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">High-Output Growth.</span>
        </h2>
        <p class="text-[rgba(255,253,217,0.75)] text-base sm:text-lg mt-3 leading-relaxed">
          Choose a package that fits your channel cadence. No contracts. Cancel or pause anytime with simple 14-day notice.
        </p>

        <!-- Pricing Toggle Switcher -->
        <div class="inline-flex items-center p-1.5 rounded-full bg-[#181616] border border-white/10 mt-8 shadow-xl">
          <button id="pricing-tab-monthly" type="button" class="px-6 py-2.5 rounded-full bg-[#e05326] text-white text-xs font-bold uppercase tracking-wider transition-all" onclick="setPricingMode('monthly')">
            Monthly Retainers (Best Value)
          </button>
          <button id="pricing-tab-packages" type="button" class="px-6 py-2.5 rounded-full text-[rgba(255,253,217,0.7)] hover:text-white text-xs font-bold uppercase tracking-wider transition-all" onclick="setPricingMode('packages')">
            Per-Video Packages
          </button>
        </div>
      </div>

      <!-- 3 Pricing Packages Grid (Slider on Mobile, 3-col on Desktop) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch mb-20 pricing-cards-track" id="pricing-cards-track">
        
        <!-- Package 1: Explore / Starter -->
        <div class="pricing-card">
          <div>
            <div class="flex items-center justify-between gap-3 mb-4">
              <span class="text-xs font-mono font-bold text-[#FFFDD9]/60 uppercase tracking-widest">STARTER</span>
              <span class="text-[11px] font-mono text-[#FFFDD9]/40 bg-white/[0.06] px-2.5 py-1 rounded-full">4 EDITS / MO</span>
            </div>

            <h3 class="text-2xl sm:text-3xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2">
              Explore Package
            </h3>
            <p class="text-xs text-[rgba(255,253,217,0.65)] leading-relaxed mb-6">
              Ideal for emerging channels, podcast hosts, and businesses publishing weekly content.
            </p>

            <div class="flex items-baseline gap-2 mb-8 pb-6 border-b border-white/[0.08]">
              <span id="price-explore" class="text-4xl sm:text-5xl font-extrabold text-[#FFFDD9] font-mono tracking-tight">$1,495</span>
              <span id="period-explore" class="text-xs font-mono text-[rgba(255,253,217,0.5)]">/ month</span>
            </div>

            <!-- Features List -->
            <div class="space-y-3.5 mb-8">
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>4 Long-Form Video Edits</strong> per month (or 1 on-demand)</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>48-Hour Guaranteed</strong> First Draft Delivery</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Dedicated Lead Editor</strong> &amp; Video Manager</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Unlimited Revisions</strong> Until 100% Satisfied</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Motion Graphics</strong>, Lower Thirds &amp; Sound FX</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Cinematic Color Grading</strong> &amp; Audio Leveling</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span>Royalty-Free Music &amp; 4K Stock Footage</span>
              </div>
            </div>
          </div>

          <a href="#booking" class="w-full py-4 rounded-xl bg-white/[0.08] hover:bg-white/[0.14] text-[#FFFDD9] text-xs font-extrabold uppercase tracking-wider text-center block transition-all border border-white/[0.1]">
            Get Started →
          </a>
        </div>

        <!-- Package 2: Trending / Growth (Most Popular) -->
        <div class="pricing-card is-popular">
          <div class="pricing-popular-badge">
            ★ MOST POPULAR • 7% DISCOUNT
          </div>

          <div>
            <div class="flex items-center justify-between gap-3 mb-4">
              <span class="text-xs font-mono font-bold text-[#e05326] uppercase tracking-widest">HIGH-VELOCITY GROWTH</span>
              <span class="text-[11px] font-mono text-[#e05326] bg-[#e05326]/10 border border-[#e05326]/30 px-2.5 py-1 rounded-full font-bold">8 EDITS + 8 SHORTS</span>
            </div>

            <h3 class="text-2xl sm:text-3xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2">
              Trending Package
            </h3>
            <p class="text-xs text-[rgba(255,253,217,0.7)] leading-relaxed mb-6">
              Our signature high-velocity package designed to scale audience reach, watch time, and AdSense RPM.
            </p>

            <div class="flex items-baseline gap-2 mb-8 pb-6 border-b border-white/[0.08]">
              <span id="price-trending" class="text-4xl sm:text-5xl font-extrabold text-[#FFFDD9] font-mono tracking-tight">$2,795</span>
              <span id="period-trending" class="text-xs font-mono text-[rgba(255,253,217,0.5)]">/ month</span>
            </div>

            <!-- Features List -->
            <div class="space-y-3.5 mb-8">
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>8 Long-Form Video Edits</strong> per month</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>8 Viral Shorts / Reels Included</strong> (Original or Reformats)</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>8 Custom High-CTR Thumbnails</strong> Included ($350 Value)</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>48-Hour Guaranteed</strong> First Draft Turnaround</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Dedicated Creative Pod</strong> (Lead Editor, Manager, Thumbnail Artist)</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Real-Time Updates Every 24 Hours</strong> + Direct Slack Chat</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Frame-Accurate Review Dashboard</strong> &amp; Unlimited Revisions</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span>100% Commercial IP Ownership &amp; Raw Project Files</span>
              </div>
            </div>
          </div>

          <a href="#booking" class="w-full py-4 rounded-xl bg-[#e05326] hover:bg-[#ff5d2e] text-white text-xs font-extrabold uppercase tracking-wider text-center block transition-all shadow-[0_4px_24px_rgba(224,83,38,0.4)] hover:scale-[1.02]">
            Start Trending Now →
          </a>
        </div>

        <!-- Package 3: Viral / Channel Scale -->
        <div class="pricing-card">
          <div>
            <div class="flex items-center justify-between gap-3 mb-4">
              <span class="text-xs font-mono font-bold text-[#FFFDD9]/60 uppercase tracking-widest">FULL CHANNEL SCALE</span>
              <span class="text-[11px] font-mono text-[#FFFDD9]/40 bg-white/[0.06] px-2.5 py-1 rounded-full">12+ EDITS &amp; MGMT</span>
            </div>

            <h3 class="text-2xl sm:text-3xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2">
              Viral Package
            </h3>
            <p class="text-xs text-[rgba(255,253,217,0.65)] leading-relaxed mb-6">
              The complete hands-off media engine for high-output creators, daily uploaders, and media brands.
            </p>

            <div class="flex items-baseline gap-2 mb-8 pb-6 border-b border-white/[0.08]">
              <span id="price-viral" class="text-4xl sm:text-5xl font-extrabold text-[#FFFDD9] font-mono tracking-tight">$4,495</span>
              <span id="period-viral" class="text-xs font-mono text-[rgba(255,253,217,0.5)]">/ month</span>
            </div>

            <!-- Features List -->
            <div class="space-y-3.5 mb-8">
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>12+ Long-Form Video Edits</strong> per month</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Unlimited Vertical Shorts</strong> &amp; Multi-Platform Reformats</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Full YouTube Channel Management</strong> &amp; Direct Uploads</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>YouTube SEO, Tagging, Chapters</strong> &amp; Description Funnels</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Custom Thumbnails with A/B/C Title Testing</strong></span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span><strong>Multiple Vetted Editors</strong> at Zero Extra Surcharge</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span>Weekly 1-on-1 Growth &amp; Retention Strategy Calls</span>
              </div>
              <div class="pricing-feature-item">
                <div class="pricing-check-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></div>
                <span>Priority 24-48h Expedited Turnaround SLA</span>
              </div>
            </div>
          </div>

          <a href="#booking" class="w-full py-4 rounded-xl bg-white/[0.08] hover:bg-white/[0.14] text-[#FFFDD9] text-xs font-extrabold uppercase tracking-wider text-center block transition-all border border-white/[0.1]">
            Scale Your Channel →
          </a>
        </div>

      </div>

      <!-- Mobile Pricing Slider Dots Indicator -->
      <div class="flex items-center justify-between mt-4 px-2 text-xs font-mono text-[rgba(255,253,217,0.65)] lg:hidden">
        <span class="inline-flex items-center gap-1.5 text-[#e05326] font-bold text-[11px]">
          <span class="inline-block animate-pulse">←</span> Swipe Packages <span class="inline-block animate-pulse">→</span>
        </span>
        <div class="flex items-center gap-1.5" id="pricing-carousel-dots">
          <button class="slider-dot active" data-index="0" aria-label="Explore"></button>
          <button class="slider-dot" data-index="1" aria-label="Trending"></button>
          <button class="slider-dot" data-index="2" aria-label="Viral"></button>
        </div>
        <span id="pricing-card-counter" class="font-bold tracking-wider text-[rgba(255,253,217,0.8)] text-[11px]">1 / 3</span>
      </div>

      <!-- All Packages Include: 8-Point Ironclad Guarantee Banner -->
      <div class="mt-16 p-8 sm:p-10 rounded-3xl bg-[rgba(20,19,19,0.7)] border border-white/[0.08] backdrop-blur-md">
        <div class="text-center max-w-2xl mx-auto mb-8">
          <span class="text-xs font-mono font-bold text-[#e05326] uppercase tracking-widest block mb-2">EVERY ORDER INCLUDES</span>
          <h3 class="text-2xl sm:text-3xl font-extrabold uppercase text-[#FFFDD9] tracking-tight">
            Our 8 Ironclad Studio Guarantees
          </h3>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> Dedicated Pod
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Exact same lead editor, manager, and thumbnail artist on every order.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> 48-Hour Turnaround
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Fast, consistent drafts delivered Monday through Saturday PST.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> Unlimited Revisions
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Leave timecoded comments directly until you are 100% satisfied.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> Motion Graphics
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Custom kinetic text, visual metaphors, and branded lower-thirds.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> Sound Design &amp; SFX
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Broadcast dialogue leveling, impact risers, and licensed tracks.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> Color Correction
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Shot-matching, skin tone perfection, and cinematic grading.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> 4K Stock Footage
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">Unlimited royalty-free B-roll from premium creator libraries.</p>
          </div>
          <div class="pricing-guarantee-card">
            <div class="text-sm font-bold text-[#FFFDD9] mb-1 flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> 100% IP Ownership
            </div>
            <p class="text-xs text-[rgba(255,253,217,0.6)] leading-relaxed">You own all raw files, final 4K renders, and complete rights.</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 8: CLIENT TESTIMONIALS (Infinite Review Carousel with Creator Proof)
       ========================================================================== -->
  <section id="testimonials" class="py-28 px-6 max-w-7xl mx-auto border-t border-[rgba(255,253,217,0.08)] overflow-hidden">
    <!-- Backwards compatible anchor -->
    <div id="confessions" style="position: absolute; top: 0;"></div>

    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.3)] text-[#e05326] text-xs font-mono font-bold uppercase tracking-widest mb-4">
        <span class="w-1.5 h-1.5 rounded-full bg-[#e05326] animate-pulse"></span>
        VERIFIED CLIENT REVIEWS &amp; CREATOR SUCCESS
      </div>
      <h2 class="text-4xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.08]">
        Loved by Creators &amp; <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">Growing Brands.</span>
      </h2>
      <p class="text-[rgba(255,253,217,0.7)] text-base sm:text-lg mt-3 leading-relaxed">
        See why creators trust Psyched Studio to handle their video editing, retention pacing, and YouTube channel growth.
      </p>

      <!-- Trust Badges & Verified Score -->
      <div class="flex flex-wrap items-center justify-center gap-6 mt-6 text-xs font-mono text-[rgba(255,253,217,0.6)]">
        <span class="flex items-center gap-1.5 text-[#e05326] font-bold">
          ★★★★★ <span class="text-[#FFFDD9]">4.98 / 5.0 RATING</span>
        </span>
        <span class="text-neutral-600">•</span>
        <span class="text-[#FFFDD9]">2.4M+ Verified Client Audience</span>
        <span class="text-neutral-600">•</span>
        <span class="text-[#FFFDD9]">140M+ Views Engineered</span>
        <span class="text-neutral-600">•</span>
        <span class="text-[#FFFDD9]">Zero Missed Deadlines</span>
      </div>
    </div>

    <!-- Infinite Magnifying Review Carousel Container -->
    <div class="relative w-full review-carousel-wrap" id="review-carousel-container">
      
      <!-- Subtle edge fade masks -->
      <div class="pointer-events-none absolute inset-y-0 left-0 w-16 sm:w-28 bg-gradient-to-r from-[#070709] to-transparent z-20"></div>
      <div class="pointer-events-none absolute inset-y-0 right-0 w-16 sm:w-28 bg-gradient-to-l from-[#070709] to-transparent z-20"></div>

      <!-- Scrolling Track -->
      <div class="review-carousel-track" id="review-carousel-track">
        
        <!-- Review 1: Paige Woolen -->
        <div class="review-card" data-review="1">
          <div class="flex items-center justify-between gap-3 mb-5">
            <span class="px-2.5 py-1 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.35)] text-[10px] font-mono font-bold text-[#e05326] uppercase">
              POLISHED SHOW FORMATS
            </span>
            <span class="text-xs text-[rgba(255,253,217,0.4)] font-mono">1M+ FOLLOWERS</span>
          </div>
          <div class="review-quote-mark">“</div>
          <p class="text-[rgba(255,253,217,0.9)] text-sm sm:text-base leading-relaxed mb-6 font-light">
            Umer is hands down one of the most dedicated and talented editors I’ve worked with! He made our show look polished, fun, and dynamic, nailed the revisions quickly, and kept everything organized and stress-free. His work ethic and attention to detail are top-notch, cannot recommend him enough!
          </p>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.1)] flex items-center gap-3.5">
            <img src="assets/clients/paige-woolen.jpg" alt="Paige Woolen" class="w-11 h-11 rounded-full object-cover border border-[#e05326]/60 shadow-[0_0_12px_rgba(224,83,38,0.3)]" loading="lazy" decoding="async">
            <div>
              <div class="font-bold text-[#FFFDD9] text-sm flex items-center gap-1.5">
                Paige Woolen
                <svg class="w-3.5 h-3.5 text-[#e05326]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </div>
              <div class="text-xs font-mono text-[#e05326]">Host &amp; Creator @paigeuncaged</div>
            </div>
          </div>
        </div>

        <!-- Review 2: Nate The Lawyer (Nathaniel Broughty) -->
        <div class="review-card" data-review="2">
          <div class="flex items-center justify-between gap-3 mb-5">
            <span class="px-2.5 py-1 rounded-full bg-[rgba(255,253,217,0.1)] border border-[rgba(255,253,217,0.2)] text-[10px] font-mono font-bold text-[#FFFDD9] uppercase">
              LEGAL ESSAYS &amp; COMMENTARY
            </span>
            <span class="text-xs text-[rgba(255,253,217,0.4)] font-mono">766K SUBS</span>
          </div>
          <div class="review-quote-mark">“</div>
          <p class="text-[rgba(255,253,217,0.9)] text-sm sm:text-base leading-relaxed mb-6 font-light">
            Fast turnaround and sharp pacing are crucial when breaking down complex legal cases in real time. Umer consistently delivers frame-accurate edits, engaging graphics, and rock-solid narrative retention without missing a deadline. Having him run our post-production timeline makes the whole process effortless.
          </p>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.1)] flex items-center gap-3.5">
            <img src="assets/clients/nate-the-lawyer.png" alt="Nathaniel Broughty" class="w-11 h-11 rounded-full object-cover border border-[#FFFDD9]/40 shadow-sm" loading="lazy" decoding="async">
            <div>
              <div class="font-bold text-[#FFFDD9] text-sm flex items-center gap-1.5">
                Nathaniel Broughty
                <svg class="w-3.5 h-3.5 text-[#e05326]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </div>
              <div class="text-xs font-mono text-[#e05326]">Host &amp; Attorney @ Nate The Lawyer</div>
            </div>
          </div>
        </div>

        <!-- Review 3: Doctor James O'Donovan -->
        <div class="review-card" data-review="3">
          <div class="flex items-center justify-between gap-3 mb-5">
            <span class="px-2.5 py-1 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.35)] text-[10px] font-mono font-bold text-[#e05326] uppercase">
              MEDICAL &amp; SCIENCE EXPLAINERS
            </span>
            <span class="text-xs text-[rgba(255,253,217,0.4)] font-mono">615K SUBS</span>
          </div>
          <div class="review-quote-mark">“</div>
          <p class="text-[rgba(255,253,217,0.9)] text-sm sm:text-base leading-relaxed mb-6 font-light">
            Working with Umer completely transformed how our channel delivers complex educational content. Pacing is crisp, retention holds high through 15-minute scientific breakdowns, and communication is seamless. His understanding of YouTube's algorithmic pacing is second to none.
          </p>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.1)] flex items-center gap-3.5">
            <img src="assets/clients/dr-james-odonovan.jpg" alt="Doctor James O'Donovan" class="w-11 h-11 rounded-full object-cover border border-[#e05326]/60 shadow-[0_0_12px_rgba(224,83,38,0.3)]" loading="lazy" decoding="async">
            <div>
              <div class="font-bold text-[#FFFDD9] text-sm flex items-center gap-1.5">
                Dr. James O'Donovan
                <svg class="w-3.5 h-3.5 text-[#e05326]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </div>
              <div class="text-xs font-mono text-[#e05326]">Physician &amp; Creator @drjamesodonovan</div>
            </div>
          </div>
        </div>

        <!-- Review 4: Dan Leeman -->
        <div class="review-card" data-review="4">
          <div class="flex items-center justify-between gap-3 mb-5">
            <span class="px-2.5 py-1 rounded-full bg-[rgba(255,253,217,0.1)] border border-[rgba(255,253,217,0.2)] text-[10px] font-mono font-bold text-[#FFFDD9] uppercase">
              B2B AUTOMATION &amp; TECH
            </span>
            <span class="text-xs text-[rgba(255,253,217,0.4)] font-mono">180K+ REACH</span>
          </div>
          <div class="review-quote-mark">“</div>
          <p class="text-[rgba(255,253,217,0.9)] text-sm sm:text-base leading-relaxed mb-6 font-light">
            I went from spending 18 hours every weekend editing tutorial workflows to dropping raw OBS screen recordings into my drive and having a polished, high-converting video 48 hours later. Reclaiming that time doubled my client consulting revenue.
          </p>
          <div class="pt-4 border-t border-[rgba(255,253,217,0.1)] flex items-center gap-3.5">
            <div class="w-11 h-11 rounded-full bg-[#1e1c1c] border border-white/20 flex items-center justify-center text-sm font-bold text-[#FFFDD9]">DL</div>
            <div>
              <div class="font-bold text-[#FFFDD9] text-sm flex items-center gap-1.5">
                Dan Leeman
                <svg class="w-3.5 h-3.5 text-[#e05326]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              </div>
              <div class="text-xs font-mono text-[#e05326]">Automation Brand &amp; Creator</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 9: FREQUENTLY ASKED QUESTIONS (FAQ - Direct Tasty Edits Answers)
       ========================================================================== -->
  <section id="faq" class="py-24 px-6 max-w-5xl mx-auto border-t border-[rgba(255,253,217,0.08)]">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.3)] text-[#e05326] text-xs font-mono font-bold uppercase tracking-widest mb-4">
        CLEAR ANSWERS
      </div>
      <h2 class="text-4xl sm:text-5xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.08]">
        Frequently Asked <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">Questions.</span>
      </h2>
      <p class="text-[rgba(255,253,217,0.7)] text-base sm:text-lg mt-3 leading-relaxed">
        Everything you need to know about our video editing packages, 48-hour turnarounds, and channel growth management.
      </p>
    </div>

    <div class="space-y-4" id="faq-accordion-list">
      
      <!-- FAQ 1 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            How does your pricing work and what is included?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            You can choose a monthly retainer (best value for ongoing channels) or purchase video packages. Our standard pricing for long-form video editing starts as low as $278 per video in our high-output tier, or $1,495/month for our starter retainer. Every package includes a dedicated video editor and manager, guaranteed 48-hour turnarounds, unlimited revisions, motion graphics, audio mastering, color grading, and royalty-free stock footage &amp; music.
          </p>
        </div>
      </div>

      <!-- FAQ 2 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            What types and formats of videos do you edit?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            We edit virtually all content formats for YouTube and social media: talking heads, vlogs, video essays, podcasts, business breakdowns, product tutorials, courses, and interviews. We also produce vertical video reformats and original Shorts/Reels/TikToks with custom animated captions and kinetic b-roll. Note: We do not edit wedding videos or full 3D character animation.
          </p>
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            How do I upload and share my raw footage?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            When you join, you receive access to your private client portal where you can upload footage directly, or simply share a Google Drive, Dropbox, or Frame.io link. There’s no complicated software to learn—just drop your files and our creative team takes over from there.
          </p>
        </div>
      </div>

      <!-- FAQ 4 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            What video editing software and tech stack do you use?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            Our editors work primarily in Adobe Premiere Pro and After Effects, complemented by DaVinci Resolve for specialized color grading. We use professional sound libraries and industry-standard motion design tools to ensure broadcast-quality deliverables every single time.
          </p>
        </div>
      </div>

      <!-- FAQ 5 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            Will I have the same dedicated video editor for every order?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            Yes, 100%. You work with the exact same creative pod on every video: your video manager, dedicated lead editor, and thumbnail artist. This ensures your unique pacing, visual style, and brand identity compound with every upload instead of starting from scratch.
          </p>
        </div>
      </div>

      <!-- FAQ 6 -->
      <div class="faq-accordion-item">
        <button class="faq-trigger" aria-expanded="false">
          <span class="text-base sm:text-lg font-bold text-[#FFFDD9] tracking-tight text-left">
            Do I retain 100% full copyright and ownership of the videos?
          </span>
          <span class="faq-chevron">+</span>
        </button>
        <div class="faq-content">
          <p class="text-sm sm:text-base text-[rgba(255,253,217,0.75)] leading-relaxed">
            Yes! You maintain 100% full copyright, commercial rights, and ownership of all raw project files, exports, thumbnails, and final deliverables. We never take any royalty or claim on your content.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 10: DISCOVERY CALL & DIRECT BOOKING PORTAL
       ========================================================================== -->
  <section id="booking" class="portal-section-wrap">
    <!-- Anchor compatibility -->
    <div id="contact" style="position: absolute; top: 0;"></div>

    <!-- Minimalist Convincing Background Behind Portal -->
    <div class="portal-grid-backdrop" aria-hidden="true"></div>
    <div class="portal-ambient-glow" aria-hidden="true"></div>

    <div class="max-w-7xl mx-auto relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[rgba(224, 83, 38, 0.12)] border border-[rgba(224, 83, 38, 0.35)] text-[#e05326] text-xs font-mono font-bold uppercase tracking-wider mb-4">
          <span class="w-2 h-2 rounded-full bg-[#e05326] animate-ping"></span>
          DIRECT ONBOARDING • 2 SLOTS OPEN THIS MONTH
        </div>
        <h2 class="text-3xl sm:text-5xl md:text-6xl font-extrabold uppercase tracking-tight text-[#FFFDD9] leading-[1.05] mb-4">
          Reclaim Your Time. <span class="font-['Instrument_Serif',serif] italic font-normal text-[#e05326]">Double Your Production Value.</span>
        </h2>
        <p class="text-[rgba(255,253,217,0.75)] text-sm sm:text-base leading-relaxed">
          Select an available slot below on Cal.com for your 30-minute Channel Discovery Call, or transmit your channel link for a direct custom quote.
        </p>
      </div>

      <!-- Two-Column Interactive Container -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch booking-cards-track">
        
        <!-- Left Column: Embedded Cal.com Calendar Widget -->
        <div class="lg:col-span-7 running-border-card">
          <div class="running-border-inner">
            
            <div class="flex items-center justify-between pb-4 mb-4 border-b border-[rgba(255,253,217,0.1)] flex-shrink-0">
              <div class="flex items-center gap-2.5">
                <span class="w-2.5 h-2.5 rounded-full bg-[#e05326] animate-pulse"></span>
                <span class="font-mono text-xs font-bold text-[#FFFDD9] uppercase tracking-wider">CAL.COM VERIFIED CALENDAR</span>
              </div>
              <span class="text-[11px] font-mono text-[rgba(255,253,217,0.5)]">30-MIN STRATEGY CALL</span>
            </div>

            <!-- Cal Inline Embed Container -->
            <div id="cal-inline-booking">
              <!-- Cal inline embed code begins -->
              <div style="width:100%;height:100%;overflow:scroll" id="my-cal-inline"></div>
              <!-- Cal inline embed code ends -->
            </div>

          </div>
        </div>

        <!-- Right Column: Direct Priority Inquiry & Transmission Form -->
        <div class="lg:col-span-5 priority-transmission-box flex flex-col justify-between p-6 sm:p-8">
          <div>
            <div class="flex items-center justify-between gap-3 mb-4">
              <span class="text-xs font-mono font-bold text-[#e05326] uppercase tracking-wider">• ASYNC TRANSMISSION</span>
              <span class="text-[10px] font-mono text-[#FFFDD9]/60 bg-white/[0.06] px-2 py-0.5 rounded">DIRECT INBOX</span>
            </div>

            <h3 class="text-xl sm:text-2xl font-extrabold uppercase text-[#FFFDD9] tracking-tight mb-2">
              Prefer Direct Inquiry?
            </h3>
            <p class="text-xs text-[rgba(255,253,217,0.7)] leading-relaxed mb-6">
              Drop your channel handle and current upload cadence. We’ll review your videos and reply with a custom production plan within 12 hours.
            </p>

            <form id="transmission-form" class="space-y-4" onsubmit="handleTransmissionSubmit(event)">
              <div>
                <label class="block text-[11px] font-mono text-[rgba(255,253,217,0.7)] uppercase mb-1.5 font-bold" for="creator-name">Your Name / Brand</label>
                <input type="text" id="creator-name" required placeholder="e.g. Alex Hormozi" class="w-full px-4 py-3 rounded-xl bg-white/[0.04] border border-white/[0.1] text-xs text-[#FFFDD9] placeholder-neutral-500 focus:outline-none focus:border-[#e05326] transition-colors">
              </div>

              <div>
                <label class="block text-[11px] font-mono text-[rgba(255,253,217,0.7)] uppercase mb-1.5 font-bold" for="creator-email">Email Address</label>
                <input type="email" id="creator-email" required placeholder="alex@media.com" class="w-full px-4 py-3 rounded-xl bg-white/[0.04] border border-white/[0.1] text-xs text-[#FFFDD9] placeholder-neutral-500 focus:outline-none focus:border-[#e05326] transition-colors">
              </div>

              <div>
                <label class="block text-[11px] font-mono text-[rgba(255,253,217,0.7)] uppercase mb-1.5 font-bold" for="channel-url">YouTube Channel Link or Portfolio</label>
                <input type="text" id="channel-url" required placeholder="youtube.com/@yourchannel" class="w-full px-4 py-3 rounded-xl bg-white/[0.04] border border-white/[0.1] text-xs text-[#FFFDD9] placeholder-neutral-500 focus:outline-none focus:border-[#e05326] transition-colors">
              </div>

              <div>
                <label class="block text-[11px] font-mono text-[rgba(255,253,217,0.7)] uppercase mb-1.5 font-bold" for="monthly-cadence">Monthly Video Cadence</label>
                <select id="monthly-cadence" class="w-full px-4 py-3 rounded-xl bg-[#141313] border border-white/[0.1] text-xs text-[#FFFDD9] focus:outline-none focus:border-[#e05326] transition-colors">
                  <option value="4-long-form">4 Long-Form Videos / Month (Explore Package)</option>
                  <option value="8-long-shorts" selected>8 Long-Form + 8 Shorts (Trending Package - Most Popular)</option>
                  <option value="12-full-mgmt">12+ Videos + Full YouTube Management (Viral Package)</option>
                  <option value="custom">Custom Production Volume</option>
                </select>
              </div>

              <button type="submit" id="btn-submit-transmission" class="w-full py-3.5 rounded-xl bg-[#e05326] hover:bg-[#ff5d2e] text-white text-xs font-extrabold uppercase tracking-wider shadow-[0_4px_20px_rgba(224,83,38,0.35)] transition-all flex items-center justify-center gap-2">
                <span>Send Priority Inquiry</span>
                <span>→</span>
              </button>
            </form>

            <div id="transmission-success" class="hidden mt-4 p-4 rounded-xl bg-[#e05326]/10 border border-[#e05326]/40 text-center">
              <span class="text-xs font-mono text-[#FFFDD9] font-bold block mb-1">TRANSMISSION RECEIVED ✦</span>
              <span class="text-[11px] text-[rgba(255,253,217,0.7)]">We’ll review your channel and reply to your email within 12 hours.</span>
            </div>
          </div>

          <div class="mt-6 pt-4 border-t border-[rgba(255,253,217,0.1)] flex items-center justify-between text-[11px] font-mono text-[rgba(255,253,217,0.5)]">
            <span class="flex items-center gap-1.5 text-[#e05326] font-bold">
              <span class="w-1.5 h-1.5 rounded-full bg-[#e05326]"></span> DIRECT CONTACT
            </span>
            <span>hello@psychedstudio.com</span>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ==========================================================================
       SECTION 11: GLOBAL FOOTER
       ========================================================================== -->
  <footer class="py-16 px-6 max-w-7xl mx-auto border-t border-[rgba(255,253,217,0.08)]">
    <div class="flex flex-col md:flex-row items-center justify-between gap-8">
      <div>
        <a href="#hero" class="text-xl font-extrabold text-[#FFFDD9] uppercase font-['Plus_Jakarta_Sans',sans-serif] tracking-tight">
          PSYCHED<span class="text-[#e05326]">.</span>STUDIO
        </a>
        <p class="text-xs text-[rgba(255,253,217,0.5)] mt-1.5 font-mono">
          The #1 Video Editing &amp; Channel Growth Studio for Creators &amp; Brands.
        </p>
      </div>

      <div class="flex flex-wrap items-center gap-6 text-xs font-mono text-[rgba(255,253,217,0.7)]">
        <a href="#services" class="hover:text-white transition-colors">Services</a>
        <a href="#why-us" class="hover:text-white transition-colors">Why Us</a>
        <a href="#how-it-works" class="hover:text-white transition-colors">How It Works</a>
        <a href="#work" class="hover:text-white transition-colors">Work &amp; Proof</a>
        <a href="#pricing" class="hover:text-white transition-colors">Pricing</a>
        <a href="#faq" class="hover:text-white transition-colors">FAQ</a>
        <a href="#booking" class="hover:text-white transition-colors">Book a Call</a>
      </div>

      <div class="flex items-center gap-4 text-xs font-mono text-[rgba(255,253,217,0.5)]">
        <span class="flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-[#e05326] animate-pulse"></span>
          <span id="footer-live-utc">UTC: --:--:--</span>
        </span>
        <span>© 2026 PSYCHED STUDIO</span>
      </div>
    </div>
  </footer>
"""

    full_output = f"{head_part}\n{body_html}\n{modals_html}\n{js_raw}"
    with open('index.html', 'w') as out_f:
        out_f.write(full_output)

    print(f"Successfully generated index.html! Length: {len(full_output)}")

if __name__ == '__main__':
    build_v8()
