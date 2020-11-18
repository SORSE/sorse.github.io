require 'html-proofer'  # https://github.com/gjtorikian/html-proofer/

task default: %w[test]

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => true,
              :allow_hash_href => true,
              file_ignore: [/assets\/js\/add-to-calendar-button/],
              url_ignore: [
                  /twitter.com/,
                  /www.turing.ac.uk/,
                  /www.linkedin.com/,
                  /www.wtfpl.net/,
                  /www.nhsx.nhs.uk\/media\/documents\/NHSX_A_Buyers_Guide_to_AI_in_Health_and_Care.pdf/,
                  /www.ncl.ac.uk\/press\/articles\/archive\/2018\/11\/fintrust/,
              ],
              :typhoeus => {
                  :ssl_verifypeer => false,
                  :ssl_verifyhost => 0}
  }
  HTMLProofer.check_directory("./_site", options).run
end
