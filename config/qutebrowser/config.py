config.load_autoconfig()
import pywalQute.draw

pywalQute.draw.color(c, {
    'spacing': {
        'vertical': 2,
        'horizontal': 8
    }
})

c.url.start_pages = ["/home/nightss/startpage-master/index.html"]
c.url.default_page = '/home/nightss/startpage-master/index.html'

c.url.searchengines = {
    'DEFAULT':  'https://search.brave.com/search?hl=en&q={}',
    'g':    'https://search.google.com/search?hl=en&q={}',
    'd':    'https://duckduckgo.com/={}',
    'w':    'https://en.wikipedia.org/wiki/{}',
    'y':    'https://www.youtube.com/results?search_query={}',
    'n':    'https://nitter.net/search?f=users&q={}'
}

c.tabs.min_width = 20

# enter insert mode if focused element
# after loading the page.
c.input.insert_mode.auto_load = False

c.window.transparent = True

c.content.blocking.method = 'adblock'
c.content.blocking.adblock.lists = [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
        #"https://gitlab.com/curben/urlhaus-filter/-/raw/master/urlhaus-filter.txt",
        "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://www.i-dont-care-about-cookies.eu/abp/",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]

config.set("fileselect.handler", "external")
config.set("fileselect.single_file.command", ['urxvt', '-e', 'ranger', '--choosefile', '{}'])
config.set("fileselect.multiple_files.command", ['urxvt', '-e', 'ranger', '--choosefiles', '{}'])


c.fonts.default_family = '20pt System San Francisco Display'
c.fonts.default_size = '20pt'
c.fonts.tabs.selected = '12pt System San Francisco Display'
c.fonts.tabs.unselected = '12pt System San Francisco Display'
c.fonts.hints = '20pt System San Francisco Display'
c.fonts.keyhint = '20pt System San Francisco Display'
c.fonts.prompts = '20pt System San Francisco Display'
c.fonts.downloads = '20pt System San Francisco Display'
c.fonts.statusbar = '15pt System San Francisco Display'
c.fonts.contextmenu = '20pt System San Francisco Display'
c.fonts.messages.info = '20pt System San Francisco Display'
c.fonts.debug_console = '20pt System San Francisco Display'
c.fonts.completion.entry = '15pt System San Francisco Display'
c.fonts.completion.category = '15pt System San Francisco Display'



c.auto_save.session = False

config.bind(',B', 'hint links spawn brave-browser {hint-url}')
config.bind(',M', 'hint links spawn mpv {hint-url}')
config.bind(',P', 'config-source')
config.bind(',Y', 'hint links spawn --userscript yt-dlp {hint-url}')
config.bind(',b', 'spawn brave-browser {url}')
config.bind(',m', 'spawn mpv {url}')
config.bind(',t', 'spawn --userscript translate')
config.bind(',y', 'spawn --userscript yt-dlp {url}')
config.bind('spawn', ',b spawn brave-browser')
config.bind('xb', 'config-cycle statusbar.show always never in-mode')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind(',a', 'config-cycle content.blocking.enabled')
config.bind(',S', 'hint links open -p {hint-url}')
config.bind(',s', 'open -p')

config.set('fonts.web.size.default', 21, 'https://web.whatsapp.com/')

c.tabs.background = True
