const LinkedIn_UserName = ''
const LinkedIn_Password = ''
const puppeteer = require('puppeteer');
const fs = require('fs')

urls = [
  'linkedin.com/company/straumann-group',
  'linkedin.com/company/basf'
]

async function main () {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  page.setViewport({width: 1024, height: 720});
  const json_file = []
  if (await login(page) == false) {
    console.log('login failed\naborting all process')
    await page.screenshot({ path: 'login_failure.png' });
    await browser.close();
  };
  for (var i=0;i<=urls.length;i++) {
    let url = 'https://'+ urls[i] + '/about/'
    await visit (page, url)
    let contents = await parse(page);
    json_file.push({'url':url, ...contents})
    console.log(i," | ",{'url':url, ...contents})
    await new Promise(r => setTimeout(r, 4000));
  };
  fs.writeFileSync('company_page_data_export.json', JSON.stringify(json_file, null, 2));
  await browser.close();
};
main ();

async function parse(page) {
  const data = await page.evaluate(() => {
    let companyName = null
    try {
      companyName = document.getElementsByClassName('t-24 t-black t-bold\
      full-width')[0].innerText;
    } catch {
      companyName = null
    };
    let website = null
    try {
      website = document.getElementsByClassName('link-without-visited-state ember-view')[0].innerText;
    } catch {
      website = null
    };
    return {'companyName':companyName,'website':website};
  });
  return data;
};

async function visit (page, url) {
  try {
    await page.goto(url, { waitUntil: 'networkidle2' });
  } catch {
  };
};

async function login (page) {
  await page.goto('https://www.linkedin.com/login');
  await page.type('#username', LinkedIn_UserName);
  await page.type('#password', LinkedIn_Password);
  await page.click('#organic-div > form > div.login__form_action_container > button');
  await page.waitForNavigation({waitUntil: 'load'});
  await new Promise(r => setTimeout(r, 5000));
  if (page.url() == "https://www.linkedin.com/feed/") {
    return true;
  } else {
    return false;
  };
};
