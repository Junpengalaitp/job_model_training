pl = "PROGRAMMING_LANGUAGE"
lf = "LIBRARY_OR_FRAMEWORK"
cp = "CONCEPT"
cs = "COMPUTER_SCIENCE"
pt = "PROTOCOL"
ds = "DATA_STORAGE"
dv = "DIVISION"
we = "WORK_EXPERIENCE"
os = 'OS'
ap = 'APPROACH'
pf = 'PLATFORM'

LABELS = [pl, lf, cp, cs, pt, ds, dv, we, os, ap, pf]

pl_list = ['JavaScript', 'Javascript', 'javascript', 'JS', 'TypeScript', 'CoffeeScript', 'HTML', 'CSS', 'CSS3', 'PHP',
           'ES6', 'Java', 'ruby', 'Typescript', 'XML',
           'java', 'Kotlin', 'kotlin', 'Go', 'go', 'bash', 'C++', 'C', 'c++', 'C#', 'c#', 'Scala', 'ES2015', 'SCSS',
           'Python', 'python', 'Ruby', 'HTML5', 'ES8', 'Golang', 'Rust', "rust", 'Objective C', 'objective-c', 'Obj-C',
           'Swift', 'swift', 'Perl', 'Erlang', 'Jython', 'Elixir', 'F#', 'ES7', 'GraphQL', 'ES2015+', 'Bash Shell']

lf_list = ['React JS', 'React.js', 'react.js', 'React', 'Redux', 'EcmaScript', 'Immutable.js', 'Babel', 'Webpack', 'NPM',
           'NGINX', 'Laravel', 'Flask', 'Django', 'django', 'scikit-learn', 'Ruby on Rails', 'Rails', 'Node.js', 'NodeJS',
           'Node', 'Honeybadger', 'Apollo', 'Vue', 'Serverless', 'Numpy', 'CLI', 'React-Native', 'Symfony2', '.NET',
           'jQuery', 'JQuery', 'Koa', 'Drupal', 'Drush', "Behat", 'Symfony2 ', 'Matplotlib', 'OpenCV', 'Matplotlib,'
           'Numpy', 'SciPy', 'pytest', 'Pytorch', 'Electron', 'Mobx', 'Chef', 'Qt', 'Haml', 'Sass', 'AJAX', 'Bootstrap',
           'Jenkins', 'Backbone', 'backbone.js', 'jUnit', 'Mockito', 'Hamcrest', 'Dagger', 'Terraform', 'Ansible', 'Ajax',
           'React Native', 'AngularJS', 'Angular', 'Jest', 'Karma', 'Protractor', 'Cypress', 'Vue.js', 'VUE', 'ASP.NET',
           'Apollo Client', 'WordPress', 'ElasticSearch', 'Elasticsearch', 'Selenium', 'machine learning', 'LAMP', 'MEAN',
           'Next.js', 'torch', 'SASS', 'redux', 'npm', 'wordpress', 'Jquery', 'big data', 'webpack', 'babel', 'react',
           'Scrapy', 'Celery', 'RabbitMQ', 'Express', 'RESTify', 'Bootstrap', 'RiotJS', 'LESS', 'Spring', 'Spring boot',
           'Gradle', 'Maven', 'Magento', 'Odoo', 'Oboe', 'Sqoop', 'Hadoop', 'Spark', 'Hive', 'YARN', 'Yarn', 'Gulp',
           'Ember', 'pytorch', 'Flux',]

cp_list = ['DOM', 'JavaScript object model', 'routing', 'switching', 'MVC', 'MVVM', 'Routing', 'Scheduling']

cs_list = ['data structure', 'algorithms', 'concurrency', 'object-oriented programming', 'design patterns',
           'Computer Science', "distributed systems", 'OOP', 'Cryptography', 'computability', 'computer architecture',
           'concurrency', 'parallelism', 'Mathematics', 'Statistics']

pt_list = ['RESTful APIs', 'REST API', 'REST APIs', 'RESTful', 'TCP/IP', 'UDP', 'browser APIs', 'HTTP', 'WebSockets',
           'WebRTC', 'API', 'APIs', 'firewalls', 'Serverless', 'CORS', 'SSL', 'Paxos', 'WASAPI', 'CoreAudio', 'wasm',
           'SFTP', 'SSH', 'TLS', 'FTP', 'REST']

ds_list = ['JSON', 'PostgreSQL', 'Postgres', 'MongoDB', 'mongodb', 'MySQL', 'mysql', 'ClustrixDB', 'Redis', 'redis', 'SQL',
           'MariaDB', 'InnoDB', 'Kafka', 'Nomad, NoSQL', 'Dynamo', 'Phoenix', 'MS SQL', 'No SQL', 'Firebase', 'HBase',
           'Memcached', 'relational database', 'Oracle',  'data warehouse', 'data marts', 'Kudu', 'HBase', 'HDFS',
           'MSSQL', 'NOSQL', 'NoSQL']

dv_list = ['front-end', 'frontend engineers', 'Web Architect', 'architect', 'Full Stack', 'full stack', 'Android Developer',
           'Android engineer', 'Game Developer', 'artificial intelligence', '3D Rendering', 'architects', 'design',
           'UI designs', 'UI', 'UX', 'AI', 'Rails Engineer', 'Product Managers', 'Designers', 'CTO', 'Web Developer',
           'Full Stack Developer', 'QA testers', 'DevOps', 'frontend stack', 'frontend UIs', 'product designers',
           'Product Designers ', 'architect', 'Big Data', 'Data Engineering', 'Data Analytics', 'computer vision',
           'Full-stack', 'backend', 'front end developer', 'QA', 'Project Management', '3D animation', 'full stack software developer',
           'UX design', 'Backend', 'UI/UX designer', 'product managers', 'engineers', 'Back-end development', 'R&D',
           'Product Management', 'designers', 'back-end', 'Design', 'frontend', 'Scrum Masters', 'analysts', 'project manager',
           'full-stack', 'developers', 'designer', 'Architect', 'audio', 'front-end development', 'QA engineers',
           'backend engineers', 'product designers', 'founder', 'CEO', 'QA engineer', 'big data', 'Front-end Engineer',
           'Full Stack Engineer', 'NLP', 'Full Stack Engineers', 'full stack engineer', 'Frontend Developers',
           'back-end developers', 'Web', 'senior software engineer', 'Sr. Software Engineer', 'back end', 'front end',
           'Data Developer/Engineer']

we_list = ['5+ years of experience', '4 years of professional experience', '2-5 years of experience', '2+ years focused on',
           '2+ years of client-side Javascript experience', '5+ years experience ', '1+ years experience',
           '2 years of professional experience', '2+ years requirement', "2+ years' experience"
           '5 years professional development experience', '3+ years of WordPress development experience',
           '2-3 years of software developer experience', '5+ years of professional software development experience',
           '5+ years of industry experience', "3+ years of software engineering experience", '5+ years experience',
           '5+ years previous experience', '3+ years of Drupal experience', '5+ years of directly applicable experience',
           '20 years of experience', '5+ years of programming experience', "3-5 years' experience",
           '3+ years in a software engineering or technical architect role', '3+ years of Unity experience',
           '3+ years of Scrum Master experience', 'Significant macOS experience (+5 years)',
           '5 years of relevant software development experience', '3-6 years relevant experience',
           '5+ years of PHP experience', '3+ years audio programming experience', "2+ years' experience",
           '5+ years of software development experience', '3-5 years of relevant work experience',
           '7+ years in the software development industryExperience ', '5 years professional development experience',
           '5+ years of applicable experience', '3+ years of experience', '2 years of Ruby on Rails Experience',
           '3+ years of professional experience', '10+ years of professional engineering experience',
           '3 years of Ruby on Rails Experience', '5 years of it being Ruby on Rails',
           '3 years of relevant data development and technology experience', '8+ years programming experience',
           ]

os_list = ['Ubuntu', 'Android', 'Debian', 'iOS', 'Windows', 'Linux', 'CentOS', 'Redhat', 'RHEL', 'macOS', 'Unix']

ap_list = ['Agile', 'automated tests', 'automated testing', 'Continuous Integration', 'Continuous Delivery', 'CI/CD',
           'Scrum', 'scrum', 'XP', 'automated testing', 'Agile', 'agile', 'git', 'automation', 'TDD', 'object-oriented design',
           'Microservices', 'waterfall', 'ETL', 'JIRA', 'Capistrano', 'automated deployment', 'code-reviews', 'SCRUM',
           'pair-programming', 'Jira', 'Lean', 'Git', 'microservices', 'CI', 'refactoring', 'Unit tests', 'gitflow',
           'microservice', 'continuous integration', 'Git-Flow', 'unit testing', 'continuous delivery', 'responsive design',
           ]

pf_list = ['AWS', 'Docker', 'Kubernetes', 'Amazon Web Services', 'Google Cloud Platform', 'Google Cloud', 'GCP',
           'Microsoft Azure', 'Solr', 'Microsoft Cognitive Services', 'OpenSLES', 'Gitlab', 'WebSphere', 'Xamarin',
           'Heroku', 'Google Analytics', 'OpenStack', 'VMware', 'Github', 'Chrome plugins', 'Unity', 'Terraform',
           'Slack', 'Trello', 'Ghost Inspector', 'CircleCI', 'Google Docs', 'Google Hangouts', 'Azure', 'GitHub',
           'ERP', 'Kafka',]