from django.core.management.base import BaseCommand, CommandError
from wagtail.models import Site

from home.models import (
    FooterSettings,
    HomePage,
    NavigationLink,
    NavigationLinkGroup,
    NavbarSettings,
    SectionFormField,
    SectionFormPage,
    SectionPage,
)


def media(url, alt):
    return {"fallback_image_url": url, "image_alt": alt}


def button(label, url):
    return {"label": label, "url": url}


def card(title, description, eyebrow="", icon="", image_url="", link_label="", link_url="", meta=""):
    return {
        "eyebrow": eyebrow,
        "title": title,
        "description": f"<p>{description}</p>" if description else "",
        "icon": icon,
        "media": media(image_url, title) if image_url else {},
        "link_label": link_label,
        "link_url": link_url,
        "meta": meta,
    }


def text_item(heading, body, eyebrow="", image_url=""):
    return {
        "eyebrow": eyebrow,
        "heading": heading,
        "body": f"<p>{body}</p>" if body else "",
        "media": media(image_url, heading) if image_url else {},
    }


SERVICE_CARDS = [
    card(
        "Website & CMS",
        "Bangun rumah digital untuk brand, katalog produk, dan toko online yang bisa dikelola sendiri.",
        eyebrow="Website & CMS Development",
        icon="01",
        link_label="Detail",
        link_url="/services/erp-workflow-automation/",
    ),
    card(
        "Custom System",
        "Ubah proses manual berbasis Excel, dokumen, dan chat menjadi sistem digital yang lebih terstruktur.",
        eyebrow="Custom Business System",
        icon="02",
        link_label="Detail",
        link_url="/services/erp-workflow-automation/",
    ),
    card(
        "ERP & Automation",
        "Kelola sales, inventory, invoice, purchase, CRM, dan workflow perusahaan dalam satu sistem.",
        eyebrow="ERP & Workflow Automation",
        icon="03",
        link_label="Detail",
        link_url="/services/erp-workflow-automation/",
    ),
]


PAGES = [
    {
        "title": "Services",
        "slug": "services",
        "sections": [
            ("hero", {
                "style": "split",
                "eyebrow": "Services",
                "title": "Layanan digital yang sederhana, flat, dan fokus pada workflow bisnis.",
                "description": "<p>Pilih berdasarkan masalah utama: butuh rumah digital, sistem custom untuk workflow unik, atau ERP untuk operasional yang lebih terintegrasi.</p>",
                "media": media("https://picsum.photos/seed/services-main-1/1280/820", "Service overview"),
            }),
            ("cards", {
                "style": "horizontal",
                "eyebrow": "Services",
                "title": "Tiga layanan utama Koderstory",
                "description": "<p>Pilih layanan dari kebutuhan bisnis paling dekat: website, sistem custom, atau otomasi operasional.</p>",
                "cards": SERVICE_CARDS,
            }),
            ("content", {
                "title": "Mulai kecil, lalu dikembangkan bertahap.",
                "description": "<p>Bisnis tidak harus langsung membangun sistem besar dari awal.</p>",
                "items": [
                    text_item("Map", "Petakan proses yang paling sering menghambat tim.", "01", "https://picsum.photos/seed/v12-step-map/900/620"),
                    text_item("Build", "Bangun modul awal yang bisa dipakai dan diuji oleh operasional.", "02", "https://picsum.photos/seed/v12-step-build/900/620"),
                    text_item("Improve", "Kembangkan sistem dari data dan kebutuhan nyata setelah rilis pertama berjalan.", "03", "https://picsum.photos/seed/v12-step-improve/900/620"),
                ],
            }),
            ("cards", {
                "style": "steps",
                "eyebrow": "Implementation",
                "title": "Mulai kecil, lalu dikembangkan bertahap.",
                "description": "<p>Bisnis tidak harus langsung membangun sistem besar dari awal. Project dapat dimulai dari fitur inti yang paling penting, lalu dikembangkan setelah workflow mulai terbukti digunakan.</p>",
                "cards": [
                    card("Map", "Memahami workflow, data, user, dan masalah bisnis yang benar-benar perlu diselesaikan.", icon="01", image_url="https://picsum.photos/seed/v12-step-map/900/620"),
                    card("Build", "Membangun modul inti yang bisa dipakai untuk menyelesaikan masalah paling penting lebih dulu.", icon="02", image_url="https://picsum.photos/seed/v12-step-build/900/620"),
                    card("Improve", "Mengembangkan fitur lanjutan setelah sistem mulai dipakai dan kebutuhan operasional semakin jelas.", icon="03", image_url="https://picsum.photos/seed/v12-step-improve/900/620"),
                ],
            }),
            ("cta", {
                "title": "Belum yakin layanan mana yang paling tepat?",
                "description": "<p>Kirim gambaran workflow Anda. Kami bantu pisahkan mana kebutuhan website, sistem custom, ERP, atau integrasi.</p>",
                "primary_button": button("Diskusikan Scope Awal", "/contact/"),
            }),
        ],
        "children": [
            {
                "title": "ERP & Workflow Automation",
                "slug": "erp-workflow-automation",
                "sections": [
                    ("hero", {
                        "style": "split",
                        "eyebrow": "ERP & Workflow Automation",
                        "title": "Operasional Bisnis yang Lebih Terintegrasi dan Terukur",
                        "description": "<p>Kelola sales, inventory, invoice, purchase, CRM, dan workflow perusahaan dalam satu sistem yang lebih rapi, efisien, dan mudah dipantau.</p>",
                        "primary_button": button("Konsultasikan Project", "/contact/"),
                        "secondary_button": button("Back to Services", "/services/"),
                        "media": media("https://picsum.photos/seed/service-erp-workflow-automation-main-1/1280/820", "ERP & Workflow Automation"),
                        "gallery": [
                            media("https://picsum.photos/seed/service-erp-workflow-automation-square-2/800/800", "ERP & Workflow Automation detail"),
                            media("https://picsum.photos/seed/service-erp-workflow-automation-wide-3/1000/650", "ERP & Workflow Automation detail"),
                        ],
                    }),
                    ("cards", {
                        "style": "grid",
                        "columns": "two",
                        "cards": [
                            card(
                                "Masalah yang sering terjadi",
                                "Ketika bisnis berkembang, data customer, quotation, invoice, stok, purchase, dan laporan sering tersebar di banyak file dan divisi. Akibatnya data tidak sinkron dan management sulit mendapatkan laporan real-time.",
                                "Problem",
                            ),
                            card(
                                "Solusi yang kami bangun",
                                "Koderstory membantu perusahaan mengimplementasikan dan menyesuaikan ERP berbasis Odoo agar proses bisnis utama terhubung dalam satu platform. Implementasi dapat dimulai dari modul inti dan dikembangkan bertahap.",
                                "Our Approach",
                            ),
                        ],
                    }),
                    ("cards", {
                        "style": "checklist",
                        "eyebrow": "We Can Help With",
                        "title": "Checklist solusi yang bisa dibangun.",
                        "cards": [
                            card("Company Profile Website", "Website resmi untuk menampilkan identitas, layanan, portfolio, dan informasi penting perusahaan.", icon="✓"),
                            card("CMS-Based Website", "Website berbasis CMS agar tim internal dapat mengelola konten secara mandiri.", icon="✓"),
                            card("Online Store Website", "Website toko online sebagai kanal penjualan mandiri di luar marketplace.", icon="✓"),
                            card("Product Catalog Website", "Katalog digital untuk menampilkan kategori, gambar, harga, dan spesifikasi produk.", icon="✓"),
                            card("Landing Page Development", "Halaman khusus untuk campaign, produk, layanan, atau penawaran tertentu.", icon="✓"),
                            card("Website Integration", "Integrasi dengan form kontak, WhatsApp, analytics, CRM, atau sistem internal.", icon="✓"),
                        ],
                    }),
                    ("cta", {
                        "eyebrow": "Next Step",
                        "title": "Siap Merapikan Workflow Bisnis Anda?",
                        "description": "<p>Jika bisnis Anda mulai merasa terbatas dengan Excel, dokumen manual, marketplace, atau proses operasional yang tersebar, Koderstory dapat membantu merancang sistem digital yang lebih rapi dan scalable.</p>",
                        "primary_button": button("Diskusikan Kebutuhan Sistem", "/contact/"),
                    }),
                ],
            },
        ],
    },
    {
        "title": "Industries",
        "slug": "industries",
        "sections": [
            ("hero", {
                "style": "cover",
                "eyebrow": "Industries",
                "title": "Solusi digital untuk industri yang ingin merapikan workflow.",
                "description": "<p>Koderstory membantu bisnis yang mulai merasakan batasan dari Excel, marketplace, chat operasional, dan tools yang tidak saling terhubung.</p>",
                "media": media("https://picsum.photos/seed/koderstory-industries-cover/1800/1000", "Industry workflow systems"),
            }),
            ("cards", {
                "title": "Industri yang kami bantu",
                "description": "<p>Pilih contoh industri untuk melihat arah solusi yang bisa dikembangkan dari workflow nyata.</p>",
                "cards": [
                    card("E-commerce & Online Retail", "Online store, catalog, checkout, payment gateway, dan sales dashboard.", "Retail", "01", "https://picsum.photos/seed/industry-grid-ecommerce/900/600", "Lihat industri", "/industries/ecommerce-online-retail/"),
                    card("Food & Beverage", "Digital menu, QR ordering, online ordering, payment, dan order dashboard.", "F&B", "02", "https://picsum.photos/seed/industry-grid-fnb/900/600", "Lihat industri", "/industries/ecommerce-online-retail/"),
                    card("Manufacturing & Production", "Production order, inventory, purchase workflow, dan progress dashboard.", "Manufacturing", "03", "https://picsum.photos/seed/industry-grid-manufacturing/900/600", "Lihat industri", "/industries/ecommerce-online-retail/"),
                    card("Property & Real Estate", "Property listing, unit catalog, inquiry, CRM property, dan lead dashboard.", "Property", "04", "https://picsum.photos/seed/industry-grid-property/900/600", "Lihat industri", "/industries/ecommerce-online-retail/"),
                ],
            }),
            ("cta", {
                "title": "Industri Anda punya workflow khusus?",
                "description": "<p>Ceritakan proses utamanya. Kami bantu memetakan sistem berdasarkan cara bisnis Anda beroperasi.</p>",
                "primary_button": button("Konsultasikan Workflow", "/contact/"),
            }),
        ],
        "children": [
            {
                "title": "E-commerce & Online Retail",
                "slug": "ecommerce-online-retail",
                "sections": [
                    ("hero", {
                        "style": "split",
                        "eyebrow": "Industry",
                        "title": "E-commerce & Online Retail",
                        "description": "<p>Online store, catalog, checkout, payment gateway, dan sales dashboard.</p>",
                        "secondary_button": button("Back to Industries", "/industries/"),
                        "media": media("https://picsum.photos/seed/industry-ecommerce-online-retail-main-1/1280/820", "E-commerce & Online Retail"),
                    }),
                    ("work_summary", {
                        "eyebrow": "How Koderstory Helps",
                        "title": "How Koderstory Helps",
                        "description": "<p>Kami membantu merancang website, sistem custom, ERP, dashboard, dan workflow automation yang sesuai dengan kebutuhan operasional industri ini.</p>",
                        "media": media("https://picsum.photos/seed/industry-ecommerce-online-retail-square-2/800/800", "E-commerce & Online Retail workflow"),
                        "facts": [
                            card("Catalog & Storefront", "Produk, kategori, gambar, harga, dan informasi produk disusun lebih rapi.", icon="01"),
                            card("Checkout & Payment", "Checkout, payment gateway, dan status order dibuat lebih mudah dipantau.", icon="02"),
                            card("Sales Dashboard", "Dashboard penjualan membantu bisnis membaca order, revenue, dan performa produk.", icon="03"),
                        ],
                    }),
                    ("cards", {
                        "style": "grid",
                        "columns": "two",
                        "eyebrow": "Example Solutions",
                        "title": "Contoh solusi yang bisa dibangun",
                        "cards": [
                            card("Online Store Website", "Website toko online untuk membantu bisnis menampilkan produk, menerima pesanan, dan membangun kanal penjualan mandiri di luar marketplace.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-square-5/800/800"),
                            card("Product Catalog Website", "Katalog produk digital yang memudahkan pelanggan melihat kategori, gambar, harga, spesifikasi, dan informasi produk secara lebih rapi.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-wide-6/1000/650"),
                            card("Product Detail Page", "Halaman detail produk yang menjelaskan deskripsi, foto, variasi, harga, spesifikasi, hingga benefit produk.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-card-7/900/600"),
                            card("Cart & Checkout System", "Sistem keranjang dan checkout sederhana agar pelanggan dapat memilih produk, mengisi data pembelian, dan melanjutkan proses pembayaran.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-square-8/800/800"),
                            card("Payment Gateway Integration", "Integrasi payment gateway agar pelanggan dapat membayar melalui transfer bank, virtual account, QRIS, atau e-wallet.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-wide-9/1000/650"),
                            card("Sales Dashboard", "Dashboard untuk memantau order, revenue, produk terlaris, status pembayaran, dan performa penjualan.", icon="✓", image_url="https://picsum.photos/seed/industry-ecommerce-online-retail-card-10/900/600"),
                        ],
                    }),
                    ("cta", {
                        "eyebrow": "Next Step",
                        "title": "Siap Membangun Solusi untuk Industri Anda?",
                        "description": "<p>Ceritakan workflow, masalah operasional, atau sistem yang ingin Anda bangun. Kami akan bantu memetakan solusi digital yang paling relevan.</p>",
                        "primary_button": button("Bahas Kebutuhan", "/contact/"),
                    }),
                ],
            }
        ],
    },
    {
        "title": "Resources",
        "slug": "resources",
        "sections": [
            ("hero", {
                "style": "cover",
                "eyebrow": "Resources",
                "title": "Insight untuk membangun sistem digital yang lebih rapi.",
                "description": "<p>Kumpulan artikel, catatan pengembangan, insight teknologi, dan studi kasus untuk membantu bisnis memahami transformasi digital, workflow automation, ERP, website, dan custom business system.</p>",
                "media": media("https://picsum.photos/seed/koderstory-resources-cover/1800/1000", "Resources cover"),
            }),
            ("cards", {
                "style": "featured",
                "title": "Artikel terbaru",
                "description": "<p>Catatan praktis untuk membantu bisnis memahami kapan workflow manual perlu dirapikan menjadi sistem.</p>",
                "cards": [
                    card("Kenapa Excel Mulai Membatasi Pertumbuhan Bisnis?", "Excel sangat fleksibel di tahap awal, tetapi saat data, tim, dan proses semakin kompleks, bisnis membutuhkan sistem yang lebih terstruktur.", "Featured Article", "", "https://picsum.photos/seed/resources-main-1/1280/820", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/"),
                    card("Tanda Bisnis Mulai Membutuhkan Sistem Operasional Digital", "Beberapa sinyal sederhana yang menunjukkan bahwa Excel dan chat sudah mulai tidak cukup.", "Business Workflow", "", "https://picsum.photos/seed/resources-square-2/800/800", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/", "June 2026 · 5 min read"),
                    card("Apa Bedanya Custom Business System dan ERP?", "Memahami perbedaan sistem custom dan ERP agar bisnis bisa memilih pendekatan yang tepat.", "Technology Insight", "", "https://picsum.photos/seed/resources-wide-3/1000/650", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/", "June 2026 · 5 min read"),
                    card("Kenapa Bisnis Perlu Website Sendiri di Luar Marketplace?", "Website sendiri membantu brand membangun kanal digital yang lebih mandiri dan terkontrol.", "Website & CMS", "", "https://picsum.photos/seed/resources-card-4/900/600", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/", "June 2026 · 5 min read"),
                    card("Dari Quotation ke Invoice: Cara Merapikan Workflow Sales", "Workflow sales yang rapi membantu sales, finance, dan management bekerja dengan data yang sama.", "ERP / Odoo", "", "https://picsum.photos/seed/resources-square-5/800/800", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/", "June 2026 · 5 min read"),
                    card("Devlog: Eksperimen QR Ordering untuk Hospitality", "Catatan pengembangan sistem pemesanan berbasis QR untuk meningkatkan revenue internal hotel.", "Devlog", "", "https://picsum.photos/seed/resources-wide-6/1000/650", "Read article", "/resources/kenapa-excel-mulai-membatasi-pertumbuhan-bisnis/", "June 2026 · 5 min read"),
                ],
            }),
            ("cta", {
                "title": "Ingin membahas topik workflow bisnis Anda?",
                "description": "<p>Kami bisa bantu membaca apakah masalahnya cukup dengan website, automation kecil, atau perlu sistem operasional khusus.</p>",
                "primary_button": button("Diskusikan", "/contact/"),
            }),
        ],
        "children": [
            {
                "title": "Kenapa Excel Mulai Membatasi Pertumbuhan Bisnis?",
                "slug": "kenapa-excel-mulai-membatasi-pertumbuhan-bisnis",
                "sections": [
                    ("hero", {
                        "style": "simple",
                        "eyebrow": "Business Workflow",
                        "title": "Kenapa Excel Mulai Membatasi Pertumbuhan Bisnis?",
                        "description": "<p>Excel sangat fleksibel di tahap awal, tetapi saat data, tim, dan proses semakin kompleks, bisnis membutuhkan sistem yang lebih terstruktur.</p>",
                    }),
                    ("article_body", {
                        "meta": "Business Workflow · 6 min read",
                        "cover": media("https://picsum.photos/seed/article-medium-cover/1600/900", "Article cover"),
                        "body": [
                            ("section", text_item("Excel membantu bisnis bergerak cepat", "Di tahap awal, spreadsheet memberi fleksibilitas untuk mencatat data, membuat formula, dan membangun laporan sederhana.")),
                            ("section", text_item("Masalah muncul saat proses semakin kompleks", "Ketika banyak orang mengedit file, status pekerjaan sulit dilacak dan data penting mulai tersebar.")),
                            ("quote", "<p>Sistem yang baik bukan hanya tentang teknologi, tetapi tentang bagaimana workflow bisnis bisa berjalan lebih efisien dan mudah dipantau.</p>"),
                            ("section", text_item("Sistem digital membantu merapikan workflow", "Dengan sistem yang lebih terstruktur, bisnis dapat mengelola data, status, approval, laporan, dan workflow dalam satu platform.")),
                        ],
                    }),
                    ("cta", {
                        "title": "Punya masalah workflow yang mirip?",
                        "description": "<p>Bagikan konteks bisnis Anda agar kami bisa bantu membaca kebutuhan sistem awalnya.</p>",
                        "primary_button": button("Hubungi Koderstory", "/contact/"),
                    }),
                ],
            }
        ],
    },
    {
        "title": "Work",
        "slug": "work",
        "sections": [
            ("hero", {
                "style": "cover",
                "eyebrow": "Work",
                "title": "Project dan implementasi sistem digital untuk workflow bisnis.",
                "description": "<p>Kumpulan contoh work, studi kasus, dan konsep implementasi yang menunjukkan bagaimana Koderstory membantu bisnis merapikan proses.</p>",
                "side_note": "<p>Gunakan halaman ini sebagai portfolio, case study index, atau daftar project yang dapat dikembangkan lebih detail.</p>",
                "media": media("https://picsum.photos/seed/koderstory-services-cover/1800/1000", "Selected work cover"),
            }),
            ("cards", {
                "style": "work",
                "title": "Selected work",
                "description": "<p>Contoh implementasi sistem digital untuk kebutuhan bisnis yang spesifik.</p>",
                "cards": [
                    card("SIRASA Hospitality QR Ordering", "Konsep sistem pemesanan berbasis QR untuk hospitality.", "Hospitality", "", "https://picsum.photos/seed/work-sirasa/1200/800", "View case", "/work/sirasa-hospitality-qr-ordering/"),
                    card("BIMORA Education Admin System", "Sistem administrasi pendidikan untuk data dan proses yang lebih rapi.", "Education", "", "https://picsum.photos/seed/work-bimora/1200/800", "View case", "#"),
                    card("Retail Sales & Inventory Workflow", "Workflow retail untuk sales, stok, dan laporan operasional.", "Retail", "", "https://picsum.photos/seed/work-retail/1200/800", "View case", "#"),
                    card("Tour Booking Management", "Website paket wisata, inquiry form, jadwal availability, pembayaran DP, dan dashboard booking.", "Tour & Travel", "", "https://picsum.photos/seed/work-tour/1200/800", "View case", "#"),
                ],
            }),
            ("cta", {
                "title": "Punya workflow yang bisa menjadi case berikutnya?",
                "description": "<p>Kita bisa mulai dari scope kecil dan dokumentasikan hasilnya sebagai sistem yang mudah dipahami tim.</p>",
                "primary_button": button("Mulai Diskusi", "/contact/"),
            }),
        ],
        "children": [
            {
                "title": "SIRASA Hospitality QR Ordering",
                "slug": "sirasa-hospitality-qr-ordering",
                "sections": [
                    ("hero", {
                        "style": "simple",
                        "eyebrow": "Hospitality · QR Ordering",
                        "title": "SIRASA Hospitality QR Ordering",
                        "description": "<p>Konsep sistem pemesanan berbasis QR untuk membantu hotel mengarahkan tamu memesan menu internal dan merchant partner melalui alur yang lebih rapi.</p>",
                        "side_note": "<p><strong>Scope</strong></p><p>Digital menu, QR ordering, tenant catalog, order tracking, dashboard transaksi, dan report sederhana.</p>",
                        "secondary_button": button("Back to Work", "/work/"),
                    }),
                    ("article_body", {
                        "cover": media("https://picsum.photos/seed/work-detail-sirasa-cover/1600/900", "SIRASA project preview"),
                        "meta": "Project Summary · Industry: Hospitality · Service: Custom Business System · Focus: Guest order workflow · Stage: Concept / MVP",
                        "body": [
                            ("section", text_item("Challenge", "Hotel memiliki peluang revenue tambahan dari room service, restoran, dan merchant partner. Namun jika proses order tidak mudah diakses oleh tamu, pemesanan bisa berpindah ke platform luar.")),
                            ("section", text_item("Solution", "SIRASA dirancang sebagai sistem pemesanan berbasis QR yang dapat diakses dari kamar atau area hotel. Tamu dapat melihat menu, memilih merchant, membuat order, dan tim operasional dapat memantau status transaksi dari dashboard.")),
                            ("section", text_item("Key Features", "QR Menu & Ordering: Tamu dapat mengakses menu dan melakukan order dari QR code. Merchant Partner Catalog: Hotel dapat menampilkan restoran atau tenant partner dalam satu katalog. Transaction Dashboard: Admin dapat memantau order, status, revenue, dan laporan transaksi.")),
                            ("section", text_item("Outcome", "Dengan workflow yang lebih mudah diakses, hotel memiliki peluang untuk meningkatkan transaksi internal, memperjelas koordinasi operasional, dan membangun kanal layanan digital yang lebih terkontrol.")),
                        ],
                    }),
                    ("cta", {
                        "title": "Ingin membuat workflow digital seperti ini?",
                        "description": "<p>Kami bisa bantu menyesuaikan konsepnya dengan proses dan operasional bisnis Anda.</p>",
                        "primary_button": button("Diskusikan Project", "/contact/"),
                    }),
                ],
            }
        ],
    },
    {
        "title": "Privacy Policy",
        "slug": "privacy-policy",
        "sections": [
            ("hero", {
                "style": "simple",
                "title": "Privacy Policy",
                "description": "<p>Draft halaman privacy policy sederhana untuk website Koderstory. Sesuaikan kembali dengan kebutuhan legal, analytics, form, dan tools yang digunakan.</p>",
            }),
            ("article_body", {
                "body": [
                    ("section", text_item("Informasi yang Dikumpulkan", "Kami dapat mengumpulkan informasi yang Anda kirim melalui form kontak, email, atau komunikasi langsung.")),
                    ("section", text_item("Penggunaan Informasi", "Informasi digunakan untuk menanggapi pertanyaan, memahami kebutuhan awal, dan menyiapkan komunikasi proyek.")),
                    ("section", text_item("Kontak", "Untuk pertanyaan terkait privacy policy, hubungi kami melalui email resmi Koderstory.")),
                ],
            }),
        ],
    },
]


CONTACT_PAGE = {
    "title": "Contact",
    "slug": "contact",
    "sections": [
        ("hero", {
            "style": "cover",
            "eyebrow": "Contact",
            "title": "Punya workflow yang masih manual?",
            "description": "<p>Kirim gambaran singkat. Kami akan bantu membaca kebutuhan awal dan menentukan solusi yang paling masuk akal untuk dimulai.</p>",
            "media": media("https://picsum.photos/seed/koderstory-contact-cover/1800/1000", "Contact Koderstory"),
        }),
        ("contact", {
            "title": "Ceritakan kebutuhan awal Anda",
            "description": "<p>Tuliskan proses yang ingin dirapikan, siapa saja yang terlibat, dan hasil apa yang ingin dibuat lebih jelas.</p>",
            "cards": [
                card("Current workflow", "Bagaimana proses berjalan hari ini.", icon="01"),
                card("Main problem", "Bagian mana yang paling sering membuat tim lambat.", icon="02"),
                card("Expected outcome", "Apa hasil yang ingin lebih jelas setelah sistem dibuat.", icon="03"),
            ],
        }),
    ],
}


class Command(BaseCommand):
    help = "Delete non-home pages under the first HomePage and rebuild section-based Koderstory pages."

    def add_arguments(self, parser):
        parser.add_argument("--yes", action="store_true", help="Confirm deleting existing non-home pages under HomePage.")

    def handle(self, *args, **options):
        if not options["yes"]:
            raise CommandError("This command deletes non-home pages. Re-run with --yes to confirm.")

        homepage = HomePage.objects.first()
        if homepage is None:
            raise CommandError("No HomePage exists. Run migrations first.")

        homepage.get_children().delete()

        for page_data in PAGES:
            self._create_section_page(homepage, page_data)
        contact = self._create_form_page(homepage, CONTACT_PAGE)
        self._seed_contact_fields(contact)
        self._seed_navigation()

        self.stdout.write(self.style.SUCCESS("Section pages rebuilt."))

    def _create_section_page(self, parent, page_data):
        page = SectionPage(
            title=page_data["title"],
            slug=page_data["slug"],
            sections=page_data["sections"],
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        for child_data in page_data.get("children", []):
            self._create_section_page(page, child_data)
        return page

    def _create_form_page(self, parent, page_data):
        page = SectionFormPage(
            title=page_data["title"],
            slug=page_data["slug"],
            sections=page_data["sections"],
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        return page

    def _seed_contact_fields(self, page):
        for sort_order, (label, field_type, required, help_text) in enumerate(
            [
                ("Name", "singleline", True, ""),
                ("Email", "email", True, ""),
                ("Company", "singleline", False, ""),
                ("Project context", "multiline", True, "Tell us the workflow, problem, or system you want to discuss."),
            ]
        ):
            SectionFormField.objects.create(
                page=page,
                sort_order=sort_order,
                label=label,
                field_type=field_type,
                required=required,
                help_text=help_text,
            )

    def _seed_navigation(self):
        site = Site.objects.filter(is_default_site=True).first() or Site.objects.first()
        if not site:
            return

        NavbarSettings.objects.filter(site=site).delete()
        FooterSettings.objects.filter(site=site).delete()
        NavigationLink.objects.all().delete()
        NavigationLinkGroup.objects.all().delete()

        nav_group = NavigationLinkGroup.objects.create(name="Main navigation")
        for sort_order, (label, url) in enumerate(
            [
                ("Home", "/"),
                ("Services", "/services/"),
                ("Industries", "/industries/"),
                ("Work", "/work/"),
                ("Resources", "/resources/"),
            ],
            start=1,
        ):
            NavigationLink.objects.create(group=nav_group, label=label, url=url, sort_order=sort_order)

        NavbarSettings.objects.create(
            site=site,
            layout="logo_left_center",
            section_height=60,
            logo_text="KoderStory",
            sticky=True,
            nav_transparent=True,
            nav_group=nav_group,
            cta_label="Konsultasikan Sistem",
            cta_url="/contact/",
        )

        FooterSettings.objects.create(
            site=site,
            section_height="compact",
            copyright_text="© 2026 KoderStory. All rights reserved.",
            bottom_bar=True,
            columns=[
                ("text", {
                    "width": 50,
                    "heading": "Koderstory",
                    "body": "<p>Membantu bisnis bertransformasi dari workflow manual menjadi sistem digital yang lebih rapi dan scalable.</p>",
                }),
                ("navigation", {
                    "width": 25,
                    "heading": "Pages",
                    "nav_group": nav_group,
                }),
                ("newsletter", {
                    "width": 25,
                    "heading": "Discuss a project",
                    "description": "<p>Ceritakan workflow yang ingin dirapikan.</p>",
                    "placeholder_text": "Your email",
                    "button_label": "Contact",
                    "button_url": "/contact/",
                }),
            ],
        )
