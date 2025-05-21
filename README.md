# 12_Factor_App
Repo to understand &amp; practice 12 factor app.

Notes:
Develop stage = writing the code that defines the app
Build stage = convert the python code to a .exe file (using Python setup tools) or use docker build with config & env files. Any changes to code, no matter how minor should trigger a build release (and version update)
Production stage = program from build stage is running, and should match codebase in develop stage
