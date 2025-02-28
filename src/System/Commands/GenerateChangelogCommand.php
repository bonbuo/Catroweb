<?php

namespace App\System\Commands;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

class GenerateChangelogCommand extends Command
{
  protected function configure(): void
  {
    $this
      ->setName('changelog')
      ->setDescription('Runs auto-changelog to create a new changelog file')
      ->addArgument('file', InputArgument::REQUIRED, 'The file with additional helper functions, for default use setup.js')
    ;
  }

  protected function execute(InputInterface $input, OutputInterface $output): int
  {
    $output->writeln('Create changelog file');

    chdir('auto-changelog');

    $process = new Process(['npx', 'auto-changelog', '--handlebars-setup', $input->getArgument('file')]);
    $process->run();

    if (!$process->isSuccessful()) {
      throw new ProcessFailedException($process);
    }

    echo $process->getOutput();
    $output->writeln('Changelog file created!');

    return 0;
  }
}
